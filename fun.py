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

district_90 = read_json("s3://election-sara-artur/hu_distrcit_90.geojson")
district_94 = read_json("s3://election-sara-artur/hu_distrcit_94.geojson")
district_98 = read_json("s3://election-sara-artur/hu_distrcit_98.geojson")
district_02 = read_json("s3://election-sara-artur/hu_distrcit_02.geojson")
district_06 = read_json("s3://election-sara-artur/hu_distrcit_06.geojson")
district_10 = read_json("s3://election-sara-artur/hu_distrcit_10.geojson")
district_14 = read_json("s3://election-sara-artur/hu_distrcit_14.geojson")
district_18 = read_json("s3://election-sara-artur/hu_distrcit_18.geojson")

data_district_90 = read_json("s3://election-sara-artur/val_90.geojson")
data_district_94 = read_json("s3://election-sara-artur/val_94.geojson")
data_district_98 = read_json("s3://election-sara-artur/val_98.geojson")
data_district_02 = read_json("s3://election-sara-artur/val_02.geojson")
data_district_06 = read_json("s3://election-sara-artur/val_06.geojson")
data_district_10 = read_json("s3://election-sara-artur/val_10.geojson")
data_district_14 = read_json("s3://election-sara-artur/val_14.geojson")
data_district_18 = read_json("s3://election-sara-artur/val_18.geojson")

data_district = read_json("s3://election-sara-artur/val_90_megye.json")

hu_shape_jaras = read_json("s3://election-sara-artur/hu_jaras_90.geojson")
data_jaras = read_json("s3://election-sara-artur/val_90_jaras.json")

hu_shape_budapest = read_json("s3://election-sara-artur/hu_budapesz.geojson")
data_kerulet = read_json("s3://election-sara-artur/val_90_kerület.json")


def state_style_90(state,function=False):
    """
    Returns the style for a state in a given year
    """
    
    state_result = data_district_90[state]
    
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
            'opacity': 0.8,
            'color': color,
            "highlight" : True
        } 
    else:
        # Format for style_function
        state_style = {
             'fillOpacity': 0.8,
             'weight': 1,
             'fillColor': color,
             'color': '#000000',
             "highlight" : True}    
  
    return state_style

def style_function_90(feature):
    """
    style_function used by the GeoJson folium function
    """

    state = feature['properties']['NAME_1']
    style = state_style_90(state,function=True)
    
    return style


def state_style_94(state,function=False):
    """
    Returns the style for a state in a given year
    """
    
    state_result = data_district_94[state]
    
    #Set state colour
    if max(state_result, key=state_result.get) == "SZDSZ":
        color =  "#0783c7"#blue
    elif max(state_result, key=state_result.get) == "MSZP":
        color =  "#E71A29"  
    elif max(state_result, key=state_result.get) == "MDF":
        color = "#3C8A5A"
    elif max(state_result, key=state_result.get) == "FKGP":
        color = "#445F2B" #red
    elif max(state_result, key=state_result.get) == "FIDESZ":
        color = "#fd8100"
        
    
    #Set state style
    if function == False:
        # Format for style_dictionary
        state_style = {
            'opacity': 0.8,
            'color': color,
            "highlight" : True
        } 
    else:
        # Format for style_function
        state_style = {
             'fillOpacity': 0.8,
             'weight': 1,
             'fillColor': color,
             'color': '#000000',
             "highlight" : True}    
  
    return state_style

def style_function_94(feature):
    """
    style_function used by the GeoJson folium function
    """

    state = feature['properties']['NAME_1']
    style = state_style_94(state,function=True)
    
    return style


def state_style_98(state,function=False):
    """
    Returns the style for a state in a given year
    """
    
    state_result = data_district_98[state]
    
    #Set state colour
    if max(state_result, key=state_result.get) == "SZDSZ":
        color =  "#0783c7"#blue
    elif max(state_result, key=state_result.get) == "FKGP":
        color = "#445f2b"
    elif max(state_result, key=state_result.get) == "MIÉP":
        color = "#9E863E"
    elif max(state_result, key=state_result.get) == "MSZP":
        color = '#e71a29' #red
    elif max(state_result, key=state_result.get) == "FIDESZ":
        color = "#fd8100"
        
    
    #Set state style
    if function == False:
        # Format for style_dictionary
        state_style = {
            'opacity': 0.8,
            'color': color,
            "highlight" : True
        } 
    else:
        # Format for style_function
        state_style = {
             'fillOpacity': 0.8,
             'weight': 1,
             'fillColor': color,
             'color': '#000000',
             "highlight" : True}    
  
    return state_style

def style_function_98(feature):
    """
    style_function used by the GeoJson folium function
    """

    state = feature['properties']['NAME_1']
    style = state_style_98(state,function=True)
    
    return style



def state_style_02(state,function=False):
    """
    Returns the style for a state in a given year
    """
    
    state_result = data_district_02[state]
    
    #Set state colour
    if max(state_result, key=state_result.get) == "SZDSZ":
        color =  "#0783c7"#blue
    elif max(state_result, key=state_result.get) == "CENTRUM":
        color = "#c6adb3"
    elif max(state_result, key=state_result.get) == "MIÉP":
        color = "#9E863E"
    elif max(state_result, key=state_result.get) == "MSZP":
        color = '#e71a29' #red
    elif max(state_result, key=state_result.get) == "FIDESZ-MDF":
        color = "#fd8100"
        
    
    #Set state style
    if function == False:
        # Format for style_dictionary
        state_style = {
            'opacity': 0.8,
            'color': color,
            "highlight" : True
        } 
    else:
        # Format for style_function
        state_style = {
             'fillOpacity': 0.8,
             'weight': 1,
             'fillColor': color,
             'color': '#000000',
             "highlight" : True}    
  
    return state_style

def style_function_02(feature):
    """
    style_function used by the GeoJson folium function
    """

    state = feature['properties']['NAME_1']
    style = state_style_02(state,function=True)
    
    return style


def state_style_06(state,function=False):
    """
    Returns the style for a state in a given year
    """
    
    state_result = data_district_06[state]
    
    #Set state colour
    if max(state_result, key=state_result.get) == "SZDSZ":
        color =  "#0783c7"#blue
    elif max(state_result, key=state_result.get) == "MDF":
        color = "#3C8A5A"
    elif max(state_result, key=state_result.get) == "MIÉP-JOBBIK":
        color = "#9E863E"
    elif max(state_result, key=state_result.get) == "MSZP":
        color = '#e71a29' #red
    elif max(state_result, key=state_result.get) == "FIDESZ-KDNP":
        color = "#fd8100"
        
    
    #Set state style
    if function == False:
        # Format for style_dictionary
        state_style = {
            'opacity': 0.8,
            'color': color,
            "highlight" : True
        } 
    else:
        # Format for style_function
        state_style = {
             'fillOpacity': 0.8,
             'weight': 1,
             'fillColor': color,
             'color': '#000000',
             "highlight" : True}    
  
    return state_style

def style_function_06(feature):
    """
    style_function used by the GeoJson folium function
    """

    state = feature['properties']['NAME_1']
    style = state_style_06(state,function=True)
    
    return style


def state_style_10(state,function=False):
    """
    Returns the style for a state in a given year
    """
    
    state_result = data_district_10[state]
    
    #Set state colour
    if max(state_result, key=state_result.get) == "LMP":
        color =  "#73c92d"#blue
    elif max(state_result, key=state_result.get) == "MDF":
        color = "#3C8A5A"
    elif max(state_result, key=state_result.get) == "JOBBIK":
        color = "#008371"
    elif max(state_result, key=state_result.get) == "MSZP":
        color = '#e71a29' #red
    elif max(state_result, key=state_result.get) == "FIDESZ-KDNP":
        color = "#fd8100"
        
    
    #Set state style
    if function == False:
        # Format for style_dictionary
        state_style = {
            'opacity': 0.8,
            'color': color,
            "highlight" : True
        } 
    else:
        # Format for style_function
        state_style = {
             'fillOpacity': 0.8,
             'weight': 1,
             'fillColor': color,
             'color': '#000000',
             "highlight" : True}    
  
    return state_style

def style_function_10(feature):
    """
    style_function used by the GeoJson folium function
    """

    state = feature['properties']['NAME_1']
    style = state_style_10(state,function=True)
    
    return style


def state_style_14(state,function=False):
    """
    Returns the style for a state in a given year
    """
    
    state_result = data_district_14[state]
    
    #Set state colour
    if max(state_result, key=state_result.get) == "LMP":
        color =  "#73c92d"#blue
    elif max(state_result, key=state_result.get) == "A HAZA NEM ELADÓ":
        color = "#BF3F3F"
    elif max(state_result, key=state_result.get) == "JOBBIK":
        color = "#008371"
    elif max(state_result, key=state_result.get) == "MSZP-EGYÜTT-DK-PM-MLP":
        color = '#e71a29' #red
    elif max(state_result, key=state_result.get) == "FIDESZ-KDNP":
        color = "#fd8100"
        
    
    #Set state style
    if function == False:
        # Format for style_dictionary
        state_style = {
            'opacity': 0.8,
            'color': color,
            "highlight" : True
        } 
    else:
        # Format for style_function
        state_style = {
             'fillOpacity': 0.8,
             'weight': 1,
             'fillColor': color,
             'color': '#000000',
             "highlight" : True}    
  
    return state_style

def style_function_14(feature):
    """
    style_function used by the GeoJson folium function
    """

    state = feature['properties']['NAME_1']
    style = state_style_14(state,function=True)
    
    return style


def state_style_18(state,function=False):
    """
    Returns the style for a state in a given year
    """
    
    state_result = data_district_18[state]
    
    #Set state colour
    if max(state_result, key=state_result.get) == "LMP":
        color =  "#73c92d"#blue
    elif max(state_result, key=state_result.get) == "DK":
        color = "#007FFF"
    elif max(state_result, key=state_result.get) == "JOBBIK":
        color = "#008371"
    elif max(state_result, key=state_result.get) == "MSZP-PM":
        color = '#e71a29' #red
    elif max(state_result, key=state_result.get) == "FIDESZ-KDNP":
        color = "#fd8100"
        
    
    #Set state style
    if function == False:
        # Format for style_dictionary
        state_style = {
            'opacity': 0.8,
            'color': color,
            "highlight" : True
        } 
    else:
        # Format for style_function
        state_style = {
             'fillOpacity': 0.8,
             'weight': 1,
             'fillColor': color,
             'color': '#000000',
             "highlight" : True}    
  
    return state_style

def style_function_18(feature):
    """
    style_function used by the GeoJson folium function
    """

    state = feature['properties']['NAME_1']
    style = state_style_18(state,function=True)
    
    return style


## - ezek itt a jaras, pest

def style_function_jaras(feature):
    """
    style_function used by the GeoJson folium function
    """

    state = feature['properties']['name']
    style = state_style_90(data_jaras,state,function=True)
    
    return style
#sa
def style_function_kerulet(feature):
    """
    style_function used by the GeoJson folium function
    """

    state = feature['properties']['name']
    style = state_style_90(data_kerulet,state,function=True)
    
    return style

def highlight_style(feature): 
    """
    style_function for when choropleth button
    is highighted
    """
    return {'fillOpacity': 1,
         'weight': 1}