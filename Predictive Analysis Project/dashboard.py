import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objs as go
from datetime import datetime

# --- SETUP DASBOR ---
st.set_page_config(layout="wide", page_title="Dashboard Saham BMRI")

st.title("📈 Dashboard Analisis Saham BMRI")
data = pd.read_csv("data_bmri.csv")

# --- PREPROCESSING ---
data['Date'] = pd.to_datetime(data['Date'])
data['Year'] = data['Date'].dt.year

# --- CONTAINER 1: PERTUMBUHAN SAHAM PER TAHUN ---
with st.container():
    st.subheader("1️⃣ Pertumbuhan Harga Saham per Tahun")

    tahun_list = sorted(data['Year'].unique())
    pertumbuhan_per_tahun = []

    for tahun in tahun_list:
        data_tahun = data[data['Year'] == tahun]
        if not data_tahun.empty:
            harga_awal = data_tahun[data_tahun['Date'] == data_tahun['Date'].min()]['Close'].values.item()
            harga_akhir = data_tahun[data_tahun['Date'] == data_tahun['Date'].max()]['Close'].values.item()
            growth = ((harga_akhir - harga_awal) / harga_awal) * 100
            pertumbuhan_per_tahun.append(growth)

    warna_bars = ['#4bd659' if growth >= 0 else '#ed615c' for growth in pertumbuhan_per_tahun]

    fig1, ax1 = plt.subplots(figsize=(10, 5))
    bars = ax1.bar(tahun_list, pertumbuhan_per_tahun, color=warna_bars)
    for i, v in enumerate(pertumbuhan_per_tahun):
        ax1.text(tahun_list[i], v + (1 if v >= 0 else -1), f'{round(v, 2)}%', ha='center',
                 va='bottom' if v >= 0 else 'top', color='black', fontsize=8)
    ax1.set_xlabel('Tahun')
    ax1.set_ylabel('Persentase Pertumbuhan')
    ax1.set_title('Pertumbuhan Harga Saham BMRI per Tahun')
    ax1.grid(True)
    st.pyplot(fig1)

# --- CONTAINER 2: GRAFIK LINE PERGERAKAN HARGA ---
with st.container():
    st.subheader("2️⃣ Pergerakan Harga Saham (Line Chart)")

    fig2 = px.line(data, x='Date', y='Close',
                   title='Grafik Pergerakan Harga Saham BMRI',
                   labels={'Close': 'Harga Saham', 'Date': 'Tahun'},
                   line_shape='linear', template='plotly_dark')

    fig2.update_layout(width=1000, height=400)
    st.plotly_chart(fig2, use_container_width=True)

# --- CONTAINER 3: VOLUME SAHAM ---
with st.container():
    st.subheader("3️⃣ Volume Saham per Tahun")

    df_yearly = data.groupby('Year')['Vol.'].sum().reset_index()
    fig3, ax3 = plt.subplots(figsize=(10, 5))

    ax3.bar(df_yearly['Year'], df_yearly['Vol.'], color='red', label='Volume Saham')
    ax4 = ax3.twinx()
    ax4.plot(df_yearly['Year'], df_yearly['Vol.'], color='darkblue', marker='o', label='Tren Volume')

    ax3.set_xlabel('Tahun')
    ax3.set_ylabel('Volume Saham', color='black')
    ax4.set_ylabel('Tren Volume', color='black')
    fig3.legend(loc='upper left', bbox_to_anchor=(0.1, 0.85))
    st.pyplot(fig3)

# --- CONTAINER 4: CANDLESTICK CHART ---
with st.container():
    st.subheader("4️⃣ Grafik Candlestick Saham BMRI")

    candlestick = go.Candlestick(x=data['Date'],
                                  open=data['Open'],
                                  high=data['High'],
                                  low=data['Low'],
                                  close=data['Close'])

    layout_candle = go.Layout(
        title="Grafik Candlestick Saham BMRI",
        xaxis=dict(title='Tanggal', rangeslider=dict(visible=False)),
        yaxis=dict(title='Harga Saham (IDR)'),
        paper_bgcolor='black',
        plot_bgcolor='black',
        font=dict(color='white'),
        width=1100,
        height=500
    )

    fig4 = go.Figure(data=[candlestick], layout=layout_candle)
    st.plotly_chart(fig4, use_container_width=True)
