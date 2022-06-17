import streamlit as st
import pandas as pd
import folium
from shapely.geometry import Polygon, mapping
import json
from streamlit_folium import folium_static 

from fun.py import state_style, style_function


st.write("My First Streamlit Web App, csicskavok")

hu_shape = json.load(open('hu_distrcit.geojson', encoding = "UTF-8"))

m = folium.Map(location=[47, 20],zoom_start=7) 
choropleth =folium.GeoJson(data= hu_shape.to_json(),style_function=style_function)
folium.TileLayer('cartodbdark_matter',name="dark mode",control=True).add_to(m)

#folium.TileLayer('cartodbdark_matter',name="dark mode",control=True).add_to(m)
m.add_child(choropleth)
st.title("kezdetleges map")
folium_static(m)
