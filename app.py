# %%
import os
import requests
import streamlit as st
from dotenv import load_dotenv


# Membaca konfigurasi dari .env
# %%
load_dotenv()

# Mengambil API key
API_KEY = os.getenv("API_KEY")

# URL OpenWeather API
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

def get_weather(city):

    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }

    response = requests.get(BASE_URL, params=params)

    if response.status_code == 200:
        return response.json()

    else:
        return None

data = get_weather("Balikpapan")

if data:
    suhu = data["main"]["temp"]
    kelembapan = data["main"]["humidity"]
    kecepatan_angin = data["wind"]["speed"]
    kondisi = data["weather"][0]["description"]

    print("Suhu:", suhu)
    print("Kelembapan:", kelembapan)
    print("Kecepatan Angin:", kecepatan_angin)
    print("Kondisi:", kondisi)
else:
    print("Gagal mengambil data cuaca")

def extract_weather(data):

    weather_data = {
        "city": data["name"],
        "temperature": data["main"]["temp"],
        "humidity": data["main"]["humidity"],
        "wind_speed": data["wind"]["speed"],
        "wind_direction": data["wind"]["deg"],
        "description": data["weather"][0]["description"],
        "feels_like": data["main"]["feels_like"]
    }

    return weather_data

data = get_weather("Balikpapan")

if data:
    hasil = extract_weather(data)

    print(hasil)
else:
    print("Gagal mengambil data cuaca")

# DASHBOARD STREAMLIT

st.title("Weather Dashboard")

st.write("Monitor kondisi cuaca secara real-time.")

city = st.text_input(
    "Masukkan nama kota",
    value="Balikpapan"
)

if st.button("Cari Cuaca"):

    data = get_weather(city)

    if data:
        hasil = extract_weather(data)

        st.subheader(f"Cuaca di {hasil['city']}")

        # Baris pertama
        col1, col2 = st.columns(2)

        with col1:
            with st.container(border=True):
                st.metric(
                    "Temperature",
                    f"{hasil['temperature']} °C"
                )

        with col2:
            with st.container(border=True):
                st.metric(
                    "Feels Like",
                    f"{hasil['feels_like']} °C"
                )

        # Baris kedua
        col3, col4 = st.columns(2)

        with col3:
            with st.container(border=True):
                st.metric(
                    "Humidity",
                    f"{hasil['humidity']}%"
                )

        with col4:
            with st.container(border=True):
                st.metric(
                    "Wind Speed",
                    f"{hasil['wind_speed']} m/s"
                )