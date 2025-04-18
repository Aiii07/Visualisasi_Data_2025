import streamlit as st

st.title('Download Button')
#Creating Download Button
down_btn = st.download_button(
    label="Download Image",
    data=open("C:/xampp/htdocs/visdat/animal_wpp.jpg", "rb"),
    file_name="animal_wpp.jpg",
    mime="image/jpg"
)
st.download_button(
label="Download CSV",
data=open("./files/avocado.csv", "rb"),
file_name='data.csv',
mime='csv',
)