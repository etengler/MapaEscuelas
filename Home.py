import streamlit as st
import leafmap.foliumap as leafmap

st.set_page_config(layout="wide")

# Configuración de la página
st.title("Mapa de escuelas de Argentina")

# Crear el mapa
m = leafmap.Map(minimap_control=True)

# URLs de los servicios WMS
escuelas_wms = (
    "https://wms.ign.gob.ar/geoserver/wms?"
    "crs=EPSG:4326&dpiMode=7&format=image/png&layers=ign:puntos_de_ciencia_y_educacion_020601&styles="
)
municipios_wms = (
    "https://wms.ign.gob.ar/geoserver/wms?"
    "crs=EPSG:4326&dpiMode=7&format=image/png&layers=ign:municipio&styles="
)

# Agregar la capa de municipios al mapa
m.add_wms_layer(
    url=municipios_wms,
    layers="ign:municipio",
    name="Municipios",
    format="image/png",
    transparent=True,
)

# Crear la interfaz para seleccionar la funcionalidad
opcion = st.radio(
    "Opciones de visualización:",
    ("Ver todas las escuelas", "Filtrar escuelas por municipio"),
)

if opcion == "Ver todas las escuelas":
    # Mostrar todas las escuelas
    m.add_wms_layer(
        url=escuelas_wms,
        layers="ign:puntos_de_ciencia_y_educacion_020601",
        name="Escuelas",
        format="image/png",
        transparent=True,
    )
else:
    # Filtrar por municipio
    st.info("Seleccione un municipio para filtrar las escuelas.")
    municipios = ["Municipio1", "Municipio2", "Municipio3"]  # Reemplaza con los nombres reales
    municipio_seleccionado = st.selectbox("Municipio:", municipios)

    # En este caso, podrías necesitar lógica adicional para filtrar las escuelas
    # relacionadas con el municipio seleccionado (no soportado directamente con WMS).
    # Esto requiere un dataset procesado por separado.

# Mostrar el mapa
m.to_streamlit(height=500)
