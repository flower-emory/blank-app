# import pyjokes
import streamlit as st

import requests

response = requests.get("https://pokeapi.co/api/v2/pokemon/19/")

st.image(response.json()["sprites"]["front_default"])
# st.write(pyjokes.get_joke())
