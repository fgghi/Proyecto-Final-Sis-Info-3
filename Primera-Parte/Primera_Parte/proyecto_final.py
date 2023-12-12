import requests
from bs4 import BeautifulSoup
import re
import json
from geopy.geocoders import Nominatim
from dagster import asset, AssetIn


@asset
def get_city_data():
    url = "https://www.archdaily.cl/cl/1003731/estas-son-las-ciudades-mas-pobladas-de-america-latina-en-2023"
    response = requests.get(url)
    html_content = response.text
    soup = BeautifulSoup(html_content, 'html.parser')
    ciudades = extraer_datos_ciudades(soup)

    return ciudades


@asset
def obtener_population(p_tag):
    population_text = p_tag.get_text()
    population_match_2023 = re.search(r"Población 2023:\s*([\d,]+)", population_text)
    if population_match_2023:
        population = population_match_2023.group(1).replace(",", "")
        return population

    population_match_2022 = re.search(r"Población 2022:\s*([\d,]+)", population_text)
    if population_match_2022:
        population = population_match_2022.group(1).replace(",", "")
        return population

    return None


@asset
def obtener_coordenadas(ciudad, pais):
    geolocalizador = Nominatim(user_agent="myGeocoder")
    direccion = f"{ciudad}, {pais}"
    ubicacion = geolocalizador.geocode(direccion)

    if ubicacion:
        return ubicacion.latitude, ubicacion.longitude
    else:
        return None, None


@asset
def extraer_datos_ciudades(soup):
    ciudades = {"type": "FeatureCollection", "features": []}

    for ciudad_element in soup.find_all('h3'):
        nombre_ciudad_match = re.search(r'<a.*?>(.*?)<\/a>', str(ciudad_element))
        nombre_ciudad = nombre_ciudad_match.group(1) if nombre_ciudad_match else "No encontrado"

        pais_match = re.search(r'<a.*?>(.*?)<\/a>,\s(.*?)\s\(', str(ciudad_element))
        pais = pais_match.group(2) if pais_match else "No encontrado"

        poblacion_element = ciudad_element.find_next('p')
        poblacion_2023 = obtener_population(poblacion_element)

        if nombre_ciudad != "No encontrado" and pais != "No encontrado" and poblacion_2023:
            latitud, longitud = obtener_coordenadas(nombre_ciudad, pais)
            ciudad = {
                "type": "Feature",
                "geometry": {
                    "type": "Point",
                    "coordinates": [longitud, latitud]
                },
                "properties": {
                    "Nombre": nombre_ciudad,
                    "País": pais,
                    "Población 2023": poblacion_2023
                }
            }
            ciudades["features"].append(ciudad)

    return ciudades


def guardar_datos_json(ciudades):
    with open("datos_ciudades.json", "w", encoding="utf-8") as geojson_file:
        json.dump(ciudades, geojson_file, ensure_ascii=False, indent=4)


def main():
    ciudades_data = get_city_data()
    guardar_datos_json(ciudades_data)


if __name__ == "__main__":
    main()
