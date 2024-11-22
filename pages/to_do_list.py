import streamlit
import streamlit as st

t = st.text_input("make your own to do list", value=None)
st.write(", t", "")

if "stuff_to_do" not in st.session_state:
    st.session_state["stuff_to_do"] = []

if st.button("Add a chex box"):
    st.session_state["stuff_to_do"].append(t)



st.write(str(st.session_state))