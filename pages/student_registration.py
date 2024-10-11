import streamlit as st
import datetime

st.title("🐚 Welcome to Zergei Junior High!")

"""
We are so not excited to have you joining us this year before you can be officially enrolled, 
we need to collect some boring information from you:
* Your full name
* Your age
* Your date of birth
* A photo for your official ID
* Which sports you have played so far
* Your favorite color
* Have you been on your official school visit yet?
* then click the submit button when you are done
"""

# EXAMPLE INPUT
full_name = st.text_input("What is your full name?")

age = st.slider("How old are you?", 1, 17,1)
birthday = st.date_input("When's your birthday", datetime.date(2019, 7, 6))
picture = st.camera_input("Take a picture")
sports = st.radio(
    "What's the sports you have done",
    [":rainbow[Soccer]", "***nothing***", "basketball"],
)
visit = st.toggle("have you visited a official school.")

if visit:
    st.write("good for you!")
color = st.color_picker("Pick A Color", "#00f900")
st.write("The current color is", color)


submit =st.button("submit", type="primary")












# EXAMPLE OUTPUT
if submit: 
    st.subheader("Student info")
    st.write("Full name:", full_name)
    st.write("I'm ", age, "years old")

    st.write("I was born on ", birthday)
    "this is your photo"
    if picture:
        st.image(picture)
    st.write("my favorite color is", color)
    st.write("visited the school?",visit)
    st.write("the sports you have done are ",sports)

if st.button("Send balloons!"):
    st.balloons()


if st.button("Send snow!"):
    st.snow()