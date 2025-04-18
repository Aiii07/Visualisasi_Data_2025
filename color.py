import streamlit as st

st.title("Select Color")
#Defining color picker
color_code = st.color_picker("Select your color")
st.header(color_code)