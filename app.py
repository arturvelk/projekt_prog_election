import streamlit as st
import pandas as pd
import folium
from shapely.geometry import Polygon, mapping
import json
from streamlit_folium import folium_static 

#from fun import state_style, style_function
data = json.load(open("sample.json", encoding = "UTF-8"))

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
             'fillOpacity': 1,
             'weight': 1,
             'fillColor': color,
             'color': '#000000'}    
  
    return state_style

def style_function(feature):
    """
    style_function used by the GeoJson folium function
    """

    state = feature['properties']['NAME_1']
    style = state_style(data,state,function=True)
    
    return style


def highlight_style(feature): 
    """
    style_function for when choropleth button
    is highighted
    """
    return {'fillOpacity': 1,
         'weight': 1}


st.write("My First Streamlit Web App, csicskavok")

hu_shape = json.load(open('hu_distrcit.geojson', encoding = "UTF-8"))

#plot choropleth button map
m = folium.Map(location=[47, 20],zoom_start=7)
choropleth =folium.GeoJson(data= hu_shape,
                           style_function=style_function,
                           highlight_function=highlight_style).add_to(m)
folium.TileLayer('cartodbdark_matter',name="dark mode",control=True).add_to(m)

m.add_child(choropleth)
folium.LayerControl().add_to(m)
#m.add_child(folium.features.GeoJsonTooltip
#                                (fields=['NAME_1'],#, "SZDSZ", "FIDESZ","MSZP","FKGP","MDF"],
#                                labels=True))
st.title("button map?")
folium_static(m)


#m = folium.Map(location=[47, 20],zoom_start=7) 
#choropleth =folium.GeoJson(data= hu_shape,style_function=style_function)
#folium.TileLayer('cartodbdark_matter',name="dark mode",control=True).add_to(m)

#folium.TileLayer('cartodbdark_matter',name="dark mode",control=True).add_to(m)
#m.add_child(choropleth)
#st.title("kezdetleges map")
#folium_static(m)
