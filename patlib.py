# %%
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

print("Lokasi Proyek:", BASE_DIR)

#%%
LOG_DIR = BASE_DIR / "logs"

#%%
LOG_DIR.mkdir(exist_ok=True)

#%%
LOG_FILE = LOG_DIR / "weather.log"

#%%
FILE_PATH = BASE_DIR / "weather_note.txt"

#%%
FILE_PATH.write_text(
    "Weather Dashboard berhasil dijalankan."
)

print("Folder tersedia:", LOG_DIR.exists())
print("Apakah folder:", LOG_DIR.is_dir())
print("Lokasi log:", LOG_FILE)


# %%
isi_file = FILE_PATH.read_text(encoding="utf-8")

print(isi_file)

# %%
