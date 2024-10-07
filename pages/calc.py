import streamlit as st 
st.write("hello")

num1 = st.number_input("num1", value=4)


num2 = st.number_input("num2", value=5)

if st.button("➕"):
    st.write("num1 + num2 =", num2+num1)

if st.button("➖"):
    st.write("num1 ➖ num2 =", num1-num2)

if st.button("✖️"):
    st.write("num1 ✖️ num2 =", num1*num2)

if st.button("➗"):
    st.write("num1 ➗ num2 =", num1/num2)