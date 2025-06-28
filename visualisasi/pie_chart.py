import streamlit as st
import matplotlib.pyplot as plt
import plotly.express as px

def show_pie_chart(data, key):
    def pola_tidur(x):
        if x < 6:
            return "Larut"
        elif 6 <= x <= 9:
            return "Teratur"
        else:
            return "Acak"

    data["pola_tidur"] = data["sleep_hours"].apply(pola_tidur)
    jumlah = data["pola_tidur"].value_counts().reset_index()
    jumlah.columns = ["pola", "jumlah"]

    fig = px.pie(jumlah,
        names="pola",
        values="jumlah",
        hole=0.4,
        height=300,
        title="Kebiasaan Tidur Mahasiswa: Teratur, Larut, Acak")
    st.plotly_chart(fig, use_container_width=True, key="pie" + key)

def show_pie_chart_static(data):
    def pola_tidur(x):
        if x < 6:
            return "Larut"
        elif 6 <= x <= 9:
            return "Teratur"
        else:
            return "Acak"

    data["pola_tidur"] = data["sleep_hours"].apply(pola_tidur)
    jumlah = data["pola_tidur"].value_counts()

    fig, ax = plt.subplots(figsize=(6, 3))
    ax.pie(jumlah, labels=jumlah.index, autopct="%1.1f%%")
    ax.set_title("Kebiasaan Tidur Mahasiswa: Teratur, Larut, Acak")
    st.pyplot(fig)

    