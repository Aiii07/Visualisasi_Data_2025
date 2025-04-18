import streamlit as st
st.title('Text Box')
#Creating Text Box
name = st.text_input("Enter your name")
st.write("Your name is", name)
# Creating Text box with 10 as character limit
name = st.text_input("Enter your Name", max_chars=10)
password = st.text_input("Enter your password", type='password')