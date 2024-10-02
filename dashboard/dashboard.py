import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Judul aplikasi
st.title('Dashboard Bike Sharing')

# Bagian 1: Memuat data
data_path = 'data/day.csv'  # Path ke dataset yang sudah diperbarui

# Memuat data ke dalam dataframe
df = pd.read_csv(data_path)
st.write("Pratinjau Data:")
st.dataframe(df.head())

# Menampilkan statistik ringkas
st.write("Ringkasan Data:")
st.write(df.describe())

# Cek apakah file ada
if os.path.exists(data_path):
    df = pd.read_csv(data_path)

    # Memeriksa kolom yang ada
    if 'workingday' not in df.columns or 'cnt' not in df.columns or 'dteday' not in df.columns:
        st.write("Kolom yang diperlukan tidak ada dalam dataset.")
    else:
        # Bagian 2: Visualisasi penggunaan sepeda antara hari kerja dan hari libur
        st.subheader('Perbandingan Penggunaan Sepeda: Hari Kerja vs Hari Libur')
        weekday_usage = df.groupby('workingday')['cnt'].mean()

        fig, ax = plt.subplots()
        ax.bar(['Hari Kerja', 'Hari Libur'], weekday_usage)
        ax.set_ylabel('Rata-rata Jumlah Pengguna')
        ax.set_title('Penggunaan Sepeda Berdasarkan Hari')
        st.pyplot(fig)

        # Bagian 3: Tren Penggunaan Sepeda dari Tahun ke Tahun
        st.subheader('Tren Penggunaan Sepeda dari Tahun ke Tahun')
        df['year'] = pd.to_datetime(df['dteday']).dt.year
        yearly_usage = df.groupby('year')['cnt'].sum()

        fig2, ax2 = plt.subplots()
        ax2.plot(yearly_usage.index, yearly_usage.values)
        ax2.set_ylabel('Jumlah Pengguna')
        ax2.set_title('Tren Penggunaan Sepeda per Tahun')
        st.pyplot(fig2)

        # Bagian 4: Memilih tahun untuk analisis lebih lanjut
        selected_year = st.selectbox('Pilih tahun untuk analisis:', yearly_usage.index)
        yearly_data = df[df['year'] == selected_year]
        st.write(f"Data untuk tahun {selected_year}:")
        st.write(yearly_data[['dteday', 'cnt']])
else:
    st.write(f'File tidak ditemukan di {data_path}')