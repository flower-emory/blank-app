import streamlit as st
import random


def get_roll(num_sides):
    roll_1 = random.randint(1,num_sides)
    roll_2 = random.randint(1,num_sides)

    return roll_1+roll_2

st.write("Roll two dice and get the result")

num_sides = st.slider("How many sides should your dice have?", min_value=2, max_value=20)

roll = get_roll(num_sides)

st.write("Roll is:", roll)  
st.button("Reset", type="primary")






         