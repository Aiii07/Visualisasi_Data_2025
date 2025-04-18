import streamlit as st
import base64

# Function to set Image as Background
def add_local_background_image_(image_path):
    with open(image_path, "rb") as img_file: 
        encoded_string = base64.b64encode(img_file.read())
    
    st.write("Image Courtesy: pinterest")  
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url(data:image/jpg;base64,{encoded_string.decode()});
            background-size: cover;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

st.write("Background Image")
# Calling image in function
add_local_background_image_("C:/xampp/htdocs/visdat/animal_wpp.jpg")




