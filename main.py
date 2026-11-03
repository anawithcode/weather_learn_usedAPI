import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")

if not API_KEY:
    raise ValueError("API KEY Belum Dikonfigurasi")

print("API KEY Berhasil Dibaca.")

def ambil_cuaca(kota):
    url = "https://api.openweathermap.org/data/2.5/weather"

    params = {
        "q": kota,
        "appid": API_KEY,
        "units": "metric"
    }

    response = requests.get(url, params=params, timeout=15)

    response.raise_for_status()

    return response.json()

data = ambil_cuaca("Balikpapan")

print(data)