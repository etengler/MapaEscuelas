import streamlit as st
import leafmap.foliumap as leafmap
import json
import os

st.set_page_config(layout="wide")

# Configuración de la página
st.title("Mapa de escuelas de Argentina")

# Crear el mapa
m = leafmap.Map(minimap_control=True)

# Cargar datos GeoJSON (asegúrate de tener los archivos locales o en URLs accesibles)
municipios_geojson = "Recursos/municipios.geojson"  # Reemplaza con la ruta real o URL
escuelas_geojson = "Recursos/escuelas.geojson"  # Reemplaza con la ruta real o URL

# Cargar los datos GeoJSON de municipios
with open(municipios_geojson, "r") as f:
    municipios_data = json.load(f)

# Extraer los valores únicos de la columna 'nam' para filtrar
opciones_municipios = sorted(
    {feature["properties"]["nam"] for feature in municipios_data["features"]}
)

# Selector de municipio
municipio_seleccionado = st.selectbox(
    "Seleccione un municipio para visualizar:", ["Todos"] + list(opciones_municipios)
)

# Cargar y mostrar las geometrías de municipios filtrados
if municipio_seleccionado == "Todos":
    # Mostrar todos los municipios
    m.add_geojson(municipios_geojson, layer_name="Todos los Municipios")
else:
    # Filtrar los municipios según el valor seleccionado en 'nam'
    municipios_filtrados = {
        "type": "FeatureCollection",
        "features": [
            feature
            for feature in municipios_data["features"]
            if feature["properties"]["nam"] == municipio_seleccionado
        ],
    }
    # Agregar los municipios filtrados al mapa
    m.add_geojson(municipios_filtrados, layer_name=f"Municipio: {municipio_seleccionado}")

# Opcional: Mostrar todas las escuelas o aplicar un filtro (se puede extender más tarde)
mostrar_escuelas = st.checkbox("Mostrar todas las escuelas")
if mostrar_escuelas:
    # Cargar y agregar la capa de escuelas
    m.add_geojson(escuelas_geojson, layer_name="Escuelas")

# Mostrar el mapa
m.to_streamlit(height=600)