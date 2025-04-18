import streamlit as st
import pandas as pd
import numpy as np
import altair as alt

df = pd.DataFrame(
    np.random.randn(10, 10),
    columns=[f'col_no_{i}' for i in range(10)]
)
# Defining multiple arguments in write function
st.write("Here is our Data", df, "Data is in dataframe format.\n", "\nwrite is Super function")

df = pd.DataFrame(
    np.random.randn(10, 2),
    columns=['a', 'b']
)
# Defining Chart
chart = alt.Chart(df).mark_bar().encode(
    x='a', y='b', tooltip=['a', 'b']
)
# Defining Chart in write() function
st.write(chart)