import streamlit as st
st.write("Hello☺️! This is a helpful daily schedule to help you be more: Fabulously Encouraging, Lovely, Incredible, Careing, Incomprehendibly Trustworthy, Yummilicious!") 

# Part 1:
# This puts some starting values in the list of todos
if "TODO_LIST" not in st.session_state:
    st.session_state["TODO_LIST"] = []

# Part 2:
# Gives you a box to write in
# And then there's a button
# If you push that button, it adds the thing you typed to the list
title = st.text_input("Add your own")
if st.button("add a thing"):
    st.session_state["TODO_LIST"].append(title)


# Part 3:
# For each item in your list, it makes a checkbox
for checkbox in st.session_state["TODO_LIST"]:
    st.checkbox(checkbox)


#st.write("SESSION STATE:")
#st.write(str(st.session_state))

