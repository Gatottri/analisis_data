import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Judul aplikasi
st.title('Dashboard Bike Sharing')

# Bagian 1: Memuat data
data_path = 'dashboard/day.csv'  # Path ke dataset yang sudah kamu berikan
df = pd.read_csv(data_path)

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
