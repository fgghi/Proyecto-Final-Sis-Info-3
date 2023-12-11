# Enunciado, el proyecto tiene dos partes


La primera parte consiste en extraer, inicialmente, los siguientes datos:
- Nombre de la ciudad
- País
- Población en 2023
- 
De la siguiente fuente: https://www.archdaily.cl/cl/1003731/estas-son-las-ciudades-mas-pobladas-de-america-latina-en-2023

Se deberá obtener la ubicación geográfica de cada ciudad empleando un servicio de geocoding. Por ejemplo https://geocode.maps.co/ (si conocen algún otro servicio, pueden usarlo). Esta primera parte deberá implementarse como una aplicación de datos de Dagster con el código en un archivo llamado 'proyecto_final.py'.


La segunda parte tiene como objetivo visualizar los datos en un mapa.

- Cada marker deberá mostrar el nombre de la ciudad, el país y su población cuando el puntero se ubique sobre el marker.
- El color del marker deberá seleccionarse de acuerdo a su población aplicando las siguientes reglas:
- Rojo: población mayor a 20 millones
- Naranja: población mayor a 10 millones y menor o igual a 20 millones
- Azul: población menor o igual a 10 millones.

Recomendaciones
- Organizar el código para facilitar su lectura
- Cada función debe centrarse en una tarea (Principio de única responsabilidad)
