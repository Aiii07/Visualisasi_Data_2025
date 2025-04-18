import streamlit as st

st.title('Multi-Select')
#Defining Multi_Select with Pre-Selection
hobbies = st.multiselect(
    'what are your hobbies',
    ['Reading', 'Cooking', 'Watching Movies/Tv Series', 'Drawing', 'Hiking', 'Playing'],
    ['Reading', 'Playing'])




