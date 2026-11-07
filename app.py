# %%
import os
import requests
import streamlit as st
from dotenv import load_dotenv
import logging
import json

#%%
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
LOG_DIR = BASE_DIR / "logs"
DATA_DIR = BASE_DIR / "data"
LOG_DIR.mkdir(exist_ok=True)
DATA_DIR.mkdir(exist_ok=True)
LOG_FILE = LOG_DIR / "weather.log"
DATA_FILE = DATA_DIR / "weather_history.json"

# %%
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
    filename=LOG_FILE,
    encoding="utf-8",
    filemode="a" # biar ketimpa
)

logger = logging.getLogger(__name__)
# %%
logger.info("Aplikasi weather Dashboard dijalankan")
logger.warning("Data curah hujan tidak tersedia")
logger.error("Contoh pesan error")


# Membaca konfigurasi dari .env
# %%
load_dotenv()

# Mengambil API key
API_KEY = os.getenv("API_KEY")

# URL OpenWeather API
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"


def get_weather(city):

    logger.info("Meminta data cuaca untuk kota: %s", city)

    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }

    try:
        response = requests.get(
            BASE_URL,
            params=params,
            timeout=10
        )

        response.raise_for_status()
        logger.info("Berhasil mengambil data cuaca")
        return response.json()
        
    except requests.exceptions.RequestException:
        logger.exception("Terjadi kesalahan saat mengambil data cuaca")
        return None


def extract_weather(data):

    weather_data = {
        "city": data["name"],
        "temperature": data["main"]["temp"],
        "humidity": data["main"]["humidity"],
        "wind_speed": data["wind"]["speed"],
        "wind_direction": data["wind"].get("deg"),
        "description": data["weather"][0]["description"],
        "feels_like": data["main"]["feels_like"]
    }

    logger.info("Data cuaca berhasil diekstrak")

    return weather_data

def save_weather(weather_data):
    if DATA_FILE.exists():
        try:
            history = json.loads(
                DATA_FILE.read_text(encoding="utf-8")
        )

        except json.JSONDecodeError:
            raise ValueError("File JSON rusak atau formatnya tidak valid")

        if not isinstance(history, list):
            raise ValueError("Format history harus berupa list")

    else:
        history = []

    history.append(weather_data)

    DATA_FILE.write_text(
        json.dumps(history, indent=4),
        encoding="utf-8"
    )

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

        save_weather(hasil)

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