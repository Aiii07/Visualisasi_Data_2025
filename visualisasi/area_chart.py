import streamlit as st
import matplotlib.pyplot as plt
import plotly.express as px

def show_area_chart(data, key):
    data = data.sort_values("sleep_hours")
    fig = px.area(data,
        x="sleep_hours",
        y="study_hours_per_day",
        height=300,
        title="Durasi Tidur vs Belajar per Hari")
    st.plotly_chart(fig, use_container_width=True, key="area" + key)

def show_area_chart_static(data):
    data = data.sort_values("sleep_hours")
    fig, ax = plt.subplots(figsize=(6, 3))
    ax.fill_between(data["sleep_hours"], data["study_hours_per_day"], color="skyblue", alpha=0.5)
    ax.set_title("Durasi Tidur vs Belajar per Hari")
    ax.set_xlabel("Jam Tidur")
    ax.set_ylabel("Jam Belajar")
    st.pyplot(fig)

    