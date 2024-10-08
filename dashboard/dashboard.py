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
        usage_by_day_type = df.groupby('holiday')['cnt'].mean().reset_index()

        fig, ax = plt.subplots(figsize=(8, 5))
        sns.barplot(x='holiday', y='cnt', data=usage_by_day_type, palette='muted', ax=ax)
        ax.set_title('Rata-rata Penggunaan Sepeda Berdasarkan Status Hari')
        ax.set_xticklabels(['Hari Kerja', 'Hari Libur'], rotation=45)
        ax.set_ylabel('Rata-rata Jumlah Pengguna Sepeda')
        ax.set_xlabel('Status Hari')
        st.pyplot(fig)

        # Bagian 4: Jumlah Total Pengguna Sepeda Berdasarkan Status Hari
        st.subheader('Jumlah Total Pengguna Sepeda Berdasarkan Status Hari (Hari Kerja vs Hari Libur)')
        total_usage_by_day_type = df.groupby('holiday')['cnt'].sum().reset_index()

        fig, ax = plt.subplots(figsize=(8, 5))
        sns.barplot(x='holiday', y='cnt', data=total_usage_by_day_type, palette='muted', ax=ax)
        ax.set_title('Jumlah Total Pengguna Sepeda Berdasarkan Status Hari')
        ax.set_xticklabels(['Hari Kerja', 'Hari Libur'], rotation=45)
        ax.set_ylabel('Jumlah Total Pengguna Sepeda')
        ax.set_xlabel('Status Hari')
        st.pyplot(fig)

        # Bagian 5: Tren Penggunaan Sepeda dari Tahun ke Tahun
        df['year'] = pd.to_datetime(df['dteday']).dt.year
        st.subheader('Rata-rata Pengguna Sepeda per Tahun')
        yearly_trend = df.groupby('year')['cnt'].mean().reset_index()

        fig, ax = plt.subplots(figsize=(10, 6))
        sns.lineplot(x='year', y='cnt', data=yearly_trend, marker='o', ax=ax)
        ax.set_title('Tren Penggunaan Sepeda dari Tahun ke Tahun')
        ax.set_ylabel('Rata-rata Jumlah Pengguna Sepeda')
        ax.set_xlabel('Tahun')
        ax.grid()
        plt.xticks(yearly_trend['year'], rotation=45)  # Putar label tahun agar lebih mudah dibaca
        st.pyplot(fig)

        # Bagian 6: Total Pengguna Sepeda per Tahun
        df['year'] = pd.to_datetime(df['dteday']).dt.year

        st.subheader('Total Pengguna Sepeda per Tahun')
        total_users_per_year = df.groupby('year')['cnt'].sum().reset_index()

        fig, ax = plt.subplots(figsize=(10, 6))
        sns.barplot(x='year', y='cnt', data=total_users_per_year, palette='viridis', ax=ax)
        ax.set_title('Total Pengguna Sepeda per Tahun')
        ax.set_ylabel('Jumlah Total Pengguna Sepeda')
        ax.set_xlabel('Tahun')
        ax.grid(axis='y')
        st.pyplot(fig)

        # Bagian 7: Perubahan Pengguna Sepeda per Tahun
        st.subheader('Perubahan Pengguna Sepeda per Tahun')
        total_users_per_year['change'] = total_users_per_year['cnt'].diff()
        total_users_per_year['change'].fillna(0, inplace=True)

        fig2, ax2 = plt.subplots(figsize=(10, 6))
        sns.lineplot(x='year', y='change', data=total_users_per_year, marker='o', color='orange', ax=ax2)
        ax2.set_title('Perubahan Pengguna Sepeda per Tahun')
        ax2.set_ylabel('Perubahan Jumlah Pengguna')
        ax2.set_xlabel('Tahun')
        ax2.grid()
        st.pyplot(fig2)
else:
    st.write(f'File tidak ditemukan di {data_path}')
