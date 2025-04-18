import streamlit as st

st.title('Creating Radio Buttons')
#Defining Radio Buttons
gender = st.radio(
    "Select your gender",
    ('Male', 'Female', 'Others'))
if gender == 'Male':
    st.write('You have selected Male.')
elif gender == 'Female':
    st.write('You have selected Female.')
else: 
    st.write('You have selected Others.')



    