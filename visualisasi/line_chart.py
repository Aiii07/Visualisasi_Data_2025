import streamlit as st
import matplotlib.pyplot as plt
import plotly.express as px

def show_line_chart(data, key):
    fig = px.line(data,
        x="sleep_hours",
        y="exam_score",
        markers=True,
        height=300,
        title="Jumlah Jam Tidur vs Nilai Akademik")
    st.plotly_chart(fig, use_container_width=True, key="line" + key)

def show_line_chart_static(data):
    fig, ax = plt.subplots(figsize=(6, 3))
    ax.plot(data["sleep_hours"], data["exam_score"], marker="o", linestyle="-", color="teal")
    ax.set_title("Jumlah Jam Tidur vs Nilai Akademik")
    ax.set_xlabel("Jam Tidur")
    ax.set_ylabel("Nilai Akademik")
    st.pyplot(fig)

    