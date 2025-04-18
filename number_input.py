import streamlit as st
#Create number input
st.number_input("Enter your number")

#Create number input
num = st.number_input("Enter your number", 0, 10, 5, 2)
st.write("Min. value is 0, \n Max. value is 10")
st.write("Default Value is 5, \n Step Size Value is 2")
st.write('Total value after adding number entered with step value is:', num)