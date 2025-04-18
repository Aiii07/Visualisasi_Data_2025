import streamlit as st
import time

st.title('Progress Bars')
#Defining Progress Bars
download = st.progress(0)
for percentage in range(100):
    time.sleep(0.1)
    download.progress(percentage+1)
st.write('Downlaod Complete')