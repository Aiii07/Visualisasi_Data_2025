import streamlit as st
import pandas as pd

# Import visualisasi
from visualisasi.line_chart import show_line_chart, show_line_chart_static
from visualisasi.bar_chart import show_bar_chart, show_bar_chart_static
from visualisasi.pie_chart import show_pie_chart, show_pie_chart_static
from visualisasi.scatter_plot import show_scatter_plot, show_scatter_plot_static
from visualisasi.area_chart import show_area_chart, show_area_chart_static

# Konfigurasi halaman
st.set_page_config(page_title="Dashboard Perbandingan Pola Tidur vs Produktivitas Akademik", layout="wide")

# Judul halaman
st.title("Dashboard Perbandingan Pola Tidur VS Produktivitas Akademik")
st.write("Aisyah Nurul Fitriah - 0110223172 | Azkiya Zahra - 0110223307 | Syavira Aulia Syamsi - 0110121127")

# Load data
data = pd.read_csv("student_data.csv")

st.markdown("---")

#  Ringkasan Visualisasi 
col1, col2 = st.columns(2)

with col1:
    # Line Chart
    st.subheader("Line Chart – Jumlah Jam Tidur vs Nilai Akademik")
    show_line_chart(data, "1")

    # Area Chart
    st.subheader("Area Chart – Durasi Tidur vs Belajar per Hari")
    show_area_chart(data, "1")

    # Scatter Plot
    st.subheader("Scatter Plot – Jam Tidur vs Skor Akademik")
    show_scatter_plot(data, "1")

with col2:
    # Pie Chart
    st.subheader("Pie Chart – Kebiasaan Tidur Mahasiswa: Teratur, Larut, Acak")
    show_pie_chart(data, "1")

    # Bar Chart
    st.subheader("Bar Chart – Jumlah Tugas vs Jam Tidur")
    show_bar_chart(data, "1")

st.markdown("---")
st.header("Detail Per Chart")
# Detail Chart

# Line Chart
st.subheader("1. Line Chart – Jumlah Jam Tidur vs Nilai Akademik")
st.caption("Visualisasi ini digunakan untuk menunjukkan tren perubahan nilai akademik berdasarkan jumlah jam tidur untuk melihat pola hubungan keduanya.")
colA, colB = st.columns(2)
with colA: st.markdown("**Interaktif**"); show_line_chart(data, "2")
with colB: st.markdown("**Statis**"); show_line_chart_static(data)

# Bar Chart
st.subheader("2. Bar Chart – Jumlah Tugas vs Jam Tidur")
st.caption("Visualisasi ini digunakan untuk membandingkan rata-rata jam tidur mahasiswa dengan jumlah tugas yang diterima untuk mengamati pengaruh volume tugas terhadap durasi tidur.")
colA, colB = st.columns(2)
with colA: st.markdown("**Interaktif**"); show_bar_chart(data, "2")
with colB: st.markdown("**Statis**"); show_bar_chart_static(data)

# Pie Chart
st.subheader("3. Pie Chart – Kebiasaan Tidur Mahasiswa: Teratur, Larut, Acak")
st.caption("Visualisasi ini digunakan untuk menunjukkan proporsi dari berbagai kebiasaan tidur mahasiswa agar terlihat mana yang paling banyak dilakukan mahasiswa.")
colA, colB = st.columns(2)
with colA: st.markdown("**Interaktif**"); show_pie_chart(data, "2")
with colB: st.markdown("**Statis**"); show_pie_chart_static(data)

# Scatter Plot
st.subheader("4. Scatter Plot – Jam Tidur vs Skor Akademik")
st.caption("Visualisasi ini digunakan untuk melihat korelasi antara jam tidur dengan skor akademik, apakah makin banyak tidur semakin bagus atau tidak ada pengaruhnya.")
colA, colB = st.columns(2)
with colA: st.markdown("**Interaktif**"); show_scatter_plot(data, "2")
with colB: st.markdown("**Statis**"); show_scatter_plot_static(data)

# Area Chart
st.subheader("5. Area Chart – Durasi Tidur vs Belajar per Hari")
st.caption("Visualisasi ini digunakan untuk membandingkan durasi tidur dan belajar mahasiswa dalam periode waktu tertentu untuk melihat pola antara kedua aktivitas tersebut dari hari ke hari.")
colA, colB = st.columns(2)
with colA: st.markdown("**Interaktif**"); show_area_chart(data, "2")
with colB: st.markdown("**Statis**"); show_area_chart_static(data)

