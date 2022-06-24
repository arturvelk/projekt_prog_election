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

# @st.experimental_memo(ttl=600)


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


hu_shape_district = read_json("s3://election-sara-artur/hu_distrcit.geojson")
data_district = read_json("s3://election-sara-artur/sample.json")

hu_shape_jaras = read_json("s3://election-sara-artur/hu_jaras_90.geojson")
data_jaras = read_json("s3://election-sara-artur/val_90_jaras.json")

hu_shape_budapest = read_json("s3://election-sara-artur/hu_budapesz.geojson")
data_kerulet = read_json("s3://election-sara-artur/val_90_kerület.json")


st.write("My First Streamlit Web App, csicskavok, csicska")

select_data = st.sidebar.selectbox(
    "What data do you want to see?", ("Megyek", "Jarasok", "Budapest")
)

select_year = st.sidebar.select_slider(
    "Melyik év legyen?",
    options=["1990", "1994", "1998", "2002", "2006", "2010", "2014", "2018"],
)

dicts_year = {
    "1990": style_function_90,
    "1994": style_function_94,
    "1998": style_function_98,
    "2002": style_function_02,
    "2006": style_function_06,
    "2010": style_function_10,
    "2014": style_function_14,
    "2018": style_function_18,
}

dicts = {
    "Megyek": {
        "data": hu_shape_district,
        "style": dicts_year[select_year],
        "handler": "NAME_1",
        "helyzet": [47, 20],
        "zoom": 7,
    },
    "Jarasok": {
        "data": hu_shape_jaras,
        "style": style_function_jaras,
        "handler": "name",
        "helyzet": [47, 20],
        "zoom": 7,
    },
    "Budapest": {
        "data": hu_shape_budapest,
        "style": style_function_kerulet,
        "handler": "name",
        "helyzet": [47.5, 19.1],
        "zoom": 10.5,
    },
}

# hu_shape = json.load(open('hu_distrcit.geojson', encoding = "UTF-8")) asd
st.write(select_data)
# plot choropleth button map
def show_maps(data, style, handler, helyzet, zoom):
    m = folium.Map(location=helyzet, zoom_start=zoom)

    choropleth = (
        folium.GeoJson(
            data=data,  # jarasok vagy megyek,
            style_function=style,  # jarasok vagy megyék,
            highlight_function=highlight_style,
        )
        .add_to(m)
        .add_child(
            folium.features.GeoJsonTooltip(
                fields=[handler, "SZDSZ", "FIDESZ", "MSZP", "FKGP", "MDF"], labels=True
            )
        )
    )

    folium.TileLayer("cartodbdark_matter", name="dark mode", control=True).add_to(m)

    m.add_child(choropleth)

    folium.LayerControl().add_to(m)
    folium_static(m)


show_maps(**dicts[select_data])

# m = folium.Map(location=[47, 20],zoom_start=7)
# choropleth =folium.GeoJson(data= hu_shape,style_function=style_function)
# folium.TileLayer('cartodbdark_matter',name="dark mode",control=True).add_to(m)

# folium.TileLayer('cartodbdark_matter',name="dark mode",control=True).add_to(m)
# m.add_child(choropleth)
# st.title("kezdetleges map")
# folium_static(m)
