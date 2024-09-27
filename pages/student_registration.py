import streamlit as st
import datetime

st.title("🐚 Welcome to Zergei Junior High!")

"""
We are so excited to have you joining us this year! Before you can be officially enrolled, 
we need to collect some information from you:
* Your full name
* Your age
* Your date of birth
* A photo for your official ID
* Which sports you have played so far
* Your favorite color
* Have you been on your official school visit yet?
"""

# EXAMPLE INPUT
full_name = st.text_input("What is your full name?")

age = st.slider("How old are you?", 1, 17,1)
birthday = st.date_input("When's your birthday", datetime.date(2019, 7, 6))
picture = st.camera_input("Take a picture")
genre = st.radio(
    "What's the sports you have done",
    [":rainbow[Soccer]", "***nothing***", "basketball"],
)

color = st.color_picker("what is your favoret color", "#00f900")
on = st.toggle("have you vited a school")

if on:
    st.write("Good for you!")









# EXAMPLE OUTPUT
st.subheader("Student info")
st.write("Full name:", full_name)
st.write("I'm ", age, "years old")

st.write("I was born on ", birthday)

if picture:
    st.image(picture)
st.write("my favoet color is", color)
