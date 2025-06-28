import streamlit as st
import matplotlib.pyplot as plt
import plotly.express as px

def show_scatter_plot(data, key):
    fig = px.scatter(data,
        x="sleep_hours",
        y="exam_score",
        color="exam_score",
        size="exam_score",
        height=300,
        title="Jam Tidur vs Skor Akademik")
    st.plotly_chart(fig, use_container_width=True, key="scatter" + key)

def show_scatter_plot_static(data):
    fig, ax = plt.subplots(figsize=(6, 3))
    ax.scatter(data["sleep_hours"], data["exam_score"], color="purple")
    ax.set_title("Jam Tidur vs Skor Akademik")
    ax.set_xlabel("Jam Tidur")
    ax.set_ylabel("Skor Akademik")
    st.pyplot(fig)

    