import streamlit as st
import pandas as pd
import folium
from shapely.geometry import Polygon, mapping
import json
from streamlit_folium import folium_static 
import s3fs
import os


fs = s3fs.S3FileSystem(anon=False)

#@st.experimental_memo(ttl=600)

def read_file(filename):
    with fs.open(filename) as f:
        return f.read().decode("utf-8")

def read_json(filename):
    return json.loads(read_file(filename))
    

hu_shape = read_json("s3://election-sara-artur/hu_distrcit.geojson")
data_district = read_json("s3://election-sara-artur/sample.json")

hu_shape_jaras = read_json("s3://election-sara-artur/hu_jaras.geojson")
data_jaras = read_json("s3://election-sara-artur/sample_jaras.json")


#from fun import state_style, style_function
#data = json.load(open("sample.json", encoding = "UTF-8"))

def state_style(data, state,function=False):
    """
    Returns the style for a state in a given year
    """
    
    state_result = data[state]
    
    #Set state colour
    if max(state_result, key=state_result.get) == "SZDSZ":
        color =  "#0783c7"#blue
    elif max(state_result, key=state_result.get) == "FKGP":
        color = "#445f2b"
    elif max(state_result, key=state_result.get) == "MDF":
        color = "#3c8a5a"
    elif max(state_result, key=state_result.get) == "MSZP":
        color = '#e71a29' #red
    elif max(state_result, key=state_result.get) == "FIDESZ":
        color = "#fd8100"
        
    
    #Set state style
    if function == False:
        # Format for style_dictionary
        state_style = {
            'opacity': 1,
            'color': color,
        } 
    else:
        # Format for style_function
        state_style = {
             'fillOpacity': 0.7,
             'weight': 1,
             'fillColor': color,
             'color': '#000000'}    
  
    return state_style

def style_function_district(feature):
    """
    style_function used by the GeoJson folium function
    """

    state = feature['properties']['NAME_1']
    style = state_style(data_district,state,function=True)
    
    return style

def style_function_jaras(feature):
    """
    style_function used by the GeoJson folium function
    """

    state = feature['properties']['name']
    style = state_style(data_jaras,state,function=True)
    
    return style


def highlight_style(feature): 
    """
    style_function for when choropleth button
    is highighted
    """
    return {'fillOpacity': 1,
         'weight': 1}




st.write("My First Streamlit Web App, csicskavok, csicska")

#hu_shape = json.load(open('hu_distrcit.geojson', encoding = "UTF-8")) asd

#plot choropleth button map
m = folium.Map(location=[47, 20],zoom_start=7)
choropleth =folium.GeoJson(data= hu_shape_jaras,
                           style_function=style_function_jaras,
                           highlight_function=highlight_style).add_to(m).add_child(folium.features.GeoJsonTooltip
                                (fields=['name' ,"SZDSZ", "FIDESZ","MSZP","FKGP","MDF"],
                                labels=True))
folium.TileLayer('cartodbdark_matter',name="dark mode",control=True).add_to(m)

m.add_child(choropleth)

folium.LayerControl().add_to(m)
folium_static(m)


#m = folium.Map(location=[47, 20],zoom_start=7) 
#choropleth =folium.GeoJson(data= hu_shape,style_function=style_function)
#folium.TileLayer('cartodbdark_matter',name="dark mode",control=True).add_to(m)

#folium.TileLayer('cartodbdark_matter',name="dark mode",control=True).add_to(m)
#m.add_child(choropleth)
#st.title("kezdetleges map")
#folium_static(m)
