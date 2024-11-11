# import pyjokes
import streamlit as st

import requests
def get_image(num):
    
    response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{num}/")


    st.image(response.json()['sprites']['other']["showdown"]["front_default"], use_column_width=True)
    st.image(response.json()["sprites"]["front_default"], use_column_width=True)
num = st.slider("", 1, 130, 25)
get_image(num)






