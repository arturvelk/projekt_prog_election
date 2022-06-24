import streamlit as st
import pandas as pd
import folium
from shapely.geometry import Polygon, mapping
import json
from streamlit_folium import folium_static 
import s3fs
import os
from fun import *

fs = s3fs.S3FileSystem(anon=False)

#@st.experimental_memo(ttl=600)

def read_file(filename):
    with fs.open(filename) as f:
        return f.read().decode("utf-8")

def read_json(filename):
    return json.loads(read_file(filename))
    

hu_shape_district = read_json("s3://election-sara-artur/hu_distrcit.geojson")
data_district = read_json("s3://election-sara-artur/sample.json")

hu_shape_jaras = read_json("s3://election-sara-artur/hu_jaras_90.geojson")
data_jaras = read_json("s3://election-sara-artur/val_90_jaras.json")

hu_shape_budapest = read_json("s3://election-sara-artur/hu_budapesz.geojson")
data_kerulet = read_json("s3://election-sara-artur/val_90_kerület.json")



st.write("My First Streamlit Web App, csicskavok, csicska")

select_data = st.sidebar.selectbox("What data do you want to see?",("Megyek", "Jarasok", "Budapest"))

select_year = st.sidebar.select_slider("Melyik év legyen?", options = ["1990","1994","1998","2002","2006","2010","2014","2018"])


dicts = {"Megyek":{"data" : hu_shape_district, "style": style_function_district, "handler" : "NAME_1","helyzet" : [47,20], "zoom" : 7},
         "Jarasok":{"data" : hu_shape_jaras, "style": style_function_jaras, "handler":"name", "helyzet" : [47,20], "zoom" : 7},
         "Budapest":{"data" : hu_shape_budapest, "style": style_function_kerulet, "handler":"name", "helyzet" : [47.5, 19.1], "zoom" : 10.5}}

#hu_shape = json.load(open('hu_distrcit.geojson', encoding = "UTF-8")) asd
st.write(select_data)
#plot choropleth button map
def show_maps(data, style,handler, helyzet, zoom):
    m = folium.Map(location=helyzet,zoom_start=zoom)

    choropleth =folium.GeoJson(data= data,#jarasok vagy megyek,
                               style_function=style,#jarasok vagy megyék,
                               highlight_function=highlight_style).add_to(m).add_child(folium.features.GeoJsonTooltip
                                    (fields=[handler ,"SZDSZ", "FIDESZ","MSZP","FKGP","MDF"],
                                    labels=True))


    folium.TileLayer('cartodbdark_matter',name="dark mode",control=True).add_to(m)

    m.add_child(choropleth)

    folium.LayerControl().add_to(m)
    folium_static(m)

show_maps(**dicts[select_data])

#m = folium.Map(location=[47, 20],zoom_start=7) 
#choropleth =folium.GeoJson(data= hu_shape,style_function=style_function)
#folium.TileLayer('cartodbdark_matter',name="dark mode",control=True).add_to(m)

#folium.TileLayer('cartodbdark_matter',name="dark mode",control=True).add_to(m)
#m.add_child(choropleth)
#st.title("kezdetleges map")
#folium_static(m)
