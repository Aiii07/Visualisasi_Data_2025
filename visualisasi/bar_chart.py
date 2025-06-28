import streamlit as st
import matplotlib.pyplot as plt
import plotly.express as px

def show_bar_chart(data, key):
    data["tugas"] = data["study_hours_per_day"].round().astype(int)
    rata_tidur = data.groupby("tugas")["sleep_hours"].mean().reset_index()

    fig = px.bar(rata_tidur,
        x="tugas",
        y="sleep_hours",
        height=300,
        title="Jumlah Tugas vs Jam Tidur")
    st.plotly_chart(fig, use_container_width=True, key="bar" + key)

def show_bar_chart_static(data):
    data["tugas"] = data["study_hours_per_day"].round().astype(int)
    rata_tidur = data.groupby("tugas")["sleep_hours"].mean()

    fig, ax = plt.subplots(figsize=(6, 3))
    ax.bar(rata_tidur.index, rata_tidur.values, color="orange")
    ax.set_title("Jumlah Tugas vs Jam Tidur")
    ax.set_xlabel("Jumlah Tugas")
    ax.set_ylabel("Rata-rata Tidur")
    st.pyplot(fig)

    