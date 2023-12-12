# from .repository import data_app
from dagster import Definitions, load_assets_from_modules

from .Primera_Parte import proyecto_final

all_assets = load_assets_from_modules([proyecto_final])

defs = Definitions(
    assets=all_assets,
)