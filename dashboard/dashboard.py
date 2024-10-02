import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Judul aplikasi
st.title('Dashboard Bike Sharing')

# Bagian 1: Memuat data
data_path = 'data/day.csv'  # Path ke dataset yang sudah diperbarui

# Cek apakah file ada
if os.path.exists(data_path):
    df = pd.read_csv(data_path)
    st.write("Pratinjau Data:")
    st.dataframe(df.head())

    st.write("Ringkasan Data:")
    st.write(df.describe())

    # Memeriksa kolom yang ada
    if 'workingday' not in df.columns or 'cnt' not in df.columns or 'dteday' not in df.columns:
        st.write("Kolom yang diperlukan tidak ada dalam dataset.")
    else:
        # Bagian 2: Distribusi Jumlah Pengguna Sepeda
        st.subheader('Distribusi Jumlah Pengguna Sepeda')
        fig, ax = plt.subplots()
        sns.histplot(df['cnt'], kde=True, ax=ax)
        ax.set_xlabel('Jumlah Pengguna')
        ax.set_title('Distribusi Jumlah Pengguna Sepeda')
        st.pyplot(fig)

        # Bagian 3: Rata-rata Penggunaan Sepeda Berdasarkan Status Hari
        st.subheader('Rata-rata Penggunaan Sepeda Berdasarkan Status Hari (Hari Kerja vs Hari Libur)')
        avg_usage_by_day = df.groupby('workingday')['cnt'].mean()

        fig, ax = plt.subplots()
        ax.bar(['Hari Kerja', 'Hari Libur'], avg_usage_by_day)
        ax.set_ylabel('Rata-rata Pengguna')
        ax.set_title('Rata-rata Penggunaan Sepeda Berdasarkan Status Hari')
        st.pyplot(fig)

        # Bagian 4: Jumlah Total Pengguna Sepeda Berdasarkan Status Hari
        st.subheader('Jumlah Total Pengguna Sepeda Berdasarkan Status Hari (Hari Kerja vs Hari Libur)')
        total_usage_by_day = df.groupby('workingday')['cnt'].sum()

        fig, ax = plt.subplots()
        ax.bar(['Hari Kerja', 'Hari Libur'], total_usage_by_day, color=['blue', 'green'])
        ax.set_ylabel('Total Pengguna')
        ax.set_title('Jumlah Total Pengguna Sepeda Berdasarkan Status Hari')
        st.pyplot(fig)

        # Bagian 5: Tren Penggunaan Sepeda dari Tahun ke Tahun
        st.subheader('Tren Penggunaan Sepeda dari Tahun ke Tahun')
        df['year'] = pd.to_datetime(df['dteday']).dt.year
        yearly_usage = df.groupby('year')['cnt'].sum()

        fig, ax = plt.subplots()
        ax.plot(yearly_usage.index, yearly_usage.values, marker='o')
        ax.set_ylabel('Jumlah Pengguna')
        ax.set_title('Tren Penggunaan Sepeda dari Tahun ke Tahun')
        st.pyplot(fig)

        # Bagian 6: Total Pengguna Sepeda per Tahun
        st.subheader('Total Pengguna Sepeda per Tahun')
        fig, ax = plt.subplots()
        sns.barplot(x=yearly_usage.index, y=yearly_usage.values, ax=ax)
        ax.set_ylabel('Total Pengguna')
        ax.set_title('Total Pengguna Sepeda per Tahun')
        st.pyplot(fig)

        # Bagian 7: Perubahan Pengguna Sepeda per Tahun
        st.subheader('Perubahan Pengguna Sepeda per Tahun')
        yearly_change = yearly_usage.pct_change() * 100

        fig, ax = plt.subplots()
        ax.bar(yearly_change.index, yearly_change.values, color='purple')
        ax.set_ylabel('Perubahan Pengguna (%)')
        ax.set_title('Perubahan Pengguna Sepeda per Tahun')
        st.pyplot(fig)

        # Bagian 8: Memilih tahun untuk analisis lebih lanjut
        selected_year = st.selectbox('Pilih tahun untuk analisis:', yearly_usage.index)
        yearly_data = df[df['year'] == selected_year]
        st.write(f"Data untuk tahun {selected_year}:")
        st.write(yearly_data[['dteday', 'cnt']])
else:
    st.write(f'File tidak ditemukan di {data_path}')
