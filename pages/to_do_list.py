import streamlit
import streamlit as st

t = st.text_input("make your own to do list", value=None)
st.write("", t)

if "my_stuff" not in st.session_state:
    st.session_state["my_stuff"] = []

if st.button("Add a chex box"):
    st.session_state["my_stuff"].append(t)
    

st.write("SESSION STATE:")
st.write(str(st.session_state))