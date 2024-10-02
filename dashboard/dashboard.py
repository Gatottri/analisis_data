import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Judul dan pengenalan
st.title("Analisis Data Penyewaan Sepeda")
st.markdown('''
## Proyek Analisis Data: Dataset Penyewaan Sepeda
**Nama:** Gatot Triantono  
**Email:** gatottriantono2003@gmail.com  
**ID Dicoding:** gatot_triantono  
''')

# Bagian: Memuat data
st.header("Muat dan Eksplorasi Dataset")

# Path ke dataset
data_path = 'data/day.csv'

try:
    # Memuat data ke dalam dataframe
    df = pd.read_csv(data_path)
    st.write("Pratinjau Data:")
    st.dataframe(df.head())

    # Menampilkan statistik ringkas
    st.write("Ringkasan Data:")
    st.write(df.describe())

    # Bagian: Visualisasi
    st.header("Visualisasi")

    # Penggunaan sepeda pada hari kerja vs hari libur
    st.subheader("Penggunaan Sepeda: Hari Kerja vs Hari Libur")
    if 'holiday' in df.columns and 'count' in df.columns:
        fig, ax = plt.subplots()
        sns.barplot(x='holiday', y='count', data=df, ax=ax)
        ax.set_title("Perbandingan Penggunaan Sepeda: Hari Kerja vs Hari Libur")
        st.pyplot(fig)

    # Tren tahunan penggunaan sepeda
    st.subheader("Tren Penggunaan Sepeda Tahunan")
    if 'year' in df.columns and 'count' in df.columns:
        fig, ax = plt.subplots()
        sns.lineplot(x='year', y='count', data=df, ax=ax)
        ax.set_title("Tren Penggunaan Sepeda Tahunan")
        st.pyplot(fig)

    # Filter kustom untuk pengguna
    st.subheader("Visualisasi dengan Filter Kustom")
    if 'season' in df.columns and 'count' in df.columns:
        season_filter = st.selectbox("Pilih Musim", options=df['season'].unique())
        filtered_data = df[df['season'] == season_filter]

        fig, ax = plt.subplots()
        sns.lineplot(x='year', y='count', data=filtered_data, ax=ax)
        ax.set_title(f"Tren Penggunaan Sepeda untuk Musim: {season_filter}")
        st.pyplot(fig)

except FileNotFoundError:
    st.error(f"File {data_path} tidak ditemukan. Pastikan file tersebut ada di direktori yang benar.")
