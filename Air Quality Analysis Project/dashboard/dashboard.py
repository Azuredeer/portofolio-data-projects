import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data (Pastikan formatnya sesuai)
@st.cache_data
def load_data():
    df = pd.read_csv("dashboard/air_quality_data.csv")  # Ganti dengan file yang benar
    return df

df = load_data()

# Pastikan kolom year bertipe numerik dan ubah ke int
df["year"] = pd.to_numeric(df["year"], errors="coerce").astype("Int64")  # Gunakan Int64 untuk menangani NaN

df["hour"] = pd.to_numeric(df["hour"], errors="coerce").astype("Int64")

# Sidebar untuk memilih stasiun udara
st.sidebar.header("Pilih Stasiun Udara")
stations = df["station"].unique()
selected_station = st.sidebar.selectbox("Stasiun", stations)

# Filter data berdasarkan stasiun yang dipilih
df_filtered = df[df["station"] == selected_station].copy()

# Filter hanya tahun 2013 - 2017
df_filtered = df_filtered[(df_filtered["year"] >= 2013) & (df_filtered["year"] <= 2017)]

# Hapus nilai NaN di 'year' dan polutan sebelum plotting
pollutants = ["PM2.5", "PM10", "SO2", "NO2", "CO", "O3"]
df_filtered = df_filtered.dropna(subset=["year"] + pollutants)

# Pilihan untuk melihat berdasarkan rentang tahun
st.sidebar.header("Pilih Rentang Waktu")
year_range = st.sidebar.slider("Tahun", 2013, 2017, (2013, 2017))
df_filtered = df_filtered[(df_filtered["year"] >= year_range[0]) & (df_filtered["year"] <= year_range[1])]

# Cek apakah data kosong setelah filtering
if df_filtered.empty:
    st.warning(f"Tidak ada data untuk stasiun {selected_station} pada rentang tahun {year_range[0]}-{year_range[1]}. Pilih stasiun lain atau rentang waktu yang berbeda.")
else:
    # Layout dashboard
    st.title("Dashboard Kualitas Udara")
    st.write(f"Menampilkan data kualitas udara untuk stasiun: **{selected_station}**")

    # Pilihan untuk melihat tren berdasarkan jam
    view_by_hour = st.sidebar.checkbox("Lihat perkembangan berdasarkan jam")

    if view_by_hour:
        st.subheader("Perkembangan Polutan Setiap Jam")
        fig_hourly, axes_hourly = plt.subplots(3, 2, figsize=(15, 12))
        fig_hourly.suptitle("Rata-rata Polutan Setiap Jam", fontsize=18, fontweight="bold")

        # Atur jarak antar subplot agar tidak bentrok
        plt.subplots_adjust(hspace=0.5, wspace=0.4)

        for ax, pollutant in zip(axes_hourly.flatten(), pollutants):
            if pollutant in df_filtered.columns:
                hourly_mean = df_filtered.groupby("hour")[pollutant].mean()
                sns.lineplot(x=hourly_mean.index, y=hourly_mean, marker="o", ax=ax)
                ax.set_title(f"{pollutant}", fontsize=14, fontweight="bold")
                ax.set_xlabel("Jam", fontsize=12)
                ax.set_ylabel("Konsentrasi Polutan", fontsize=12)
                ax.grid(True)
            else:
                ax.set_visible(False)

        st.pyplot(fig_hourly)
    else:
        # Buat subplot untuk menampilkan 3 baris dan 2 kolom
        fig, axes = plt.subplots(3, 2, figsize=(15, 12))
        fig.suptitle(f"Tren Polutan Udara di Stasiun {selected_station} ({year_range[0]} - {year_range[1]})", fontsize=18, fontweight="bold")

        # Atur jarak antar subplot agar tidak bentrok
        plt.subplots_adjust(hspace=0.5, wspace=0.4)

        # Warna berbeda untuk tiap polutan agar lebih jelas
        colors = ["b", "g", "r", "c", "m", "y"]

        for ax, pollutant, color in zip(axes.flatten(), pollutants, colors):
            if pollutant in df_filtered.columns:  # Pastikan kolom polutan ada dalam dataset
                sns.lineplot(ax=ax, data=df_filtered, x="year", y=pollutant, marker="o", color=color)
                ax.set_title(f"{pollutant}", fontsize=14, fontweight="bold")
                ax.set_xlabel("Tahun", fontsize=12)
                ax.set_ylabel(f"Kadar {pollutant}", fontsize=12)
                ax.grid(True)
                ax.set_xticks(range(year_range[0], year_range[1] + 1))  # Pastikan hanya menampilkan tahun dalam rentang yang dipilih
                ax.tick_params(axis="x", rotation=45, labelsize=11)
                ax.tick_params(axis="y", labelsize=11)
            else:
                ax.set_visible(False)  # Sembunyikan subplot jika tidak ada data

        # Tampilkan plot di Streamlit
        st.pyplot(fig)
