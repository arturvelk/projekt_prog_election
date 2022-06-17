import streamlit as st
import pandas as pd
import geopandas as gpd
import folium
from shapely.geometry import Polygon, mapping
from streamlit_folium import folium_static 


st.write("My First Streamlit Web App, csicskavok")

hu_shape = gpd.read_file('map/HUN_adm1.shp')[["NAME_1","geometry"]]

m = folium.Map(location=[47, 20],zoom_start=7) 
#choropleth =folium.GeoJson(data= hu_shape.to_json())
#folium.TileLayer('cartodbdark_matter',name="dark mode",control=True).add_to(m)
#m.add_child(choropleth)
st.title("kezdetleges map")
folium_static(m)
