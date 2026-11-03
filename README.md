## 🔒 Mengapa API Key Tidak Boleh Ditulis Langsung di dalam Kode?

Menulis *API key* (kunci rahasia untuk mengakses layanan pihak ketiga seperti OpenAI, AWS, dll.) secara langsung di dalam kode (*hardcoding*) adalah praktik yang sangat berbahaya. 

### ⚠️ Risiko & Ancaman Nyata
1. **Bot *Scraper* Otomatis:** Peretas menggunakan *bot* yang memindai setiap *commit* baru di GitHub secara *real-time* dalam hitungan detik setelah Anda melakukan `git push`.
2. **Penyalahgunaan Sumber Daya:** Kunci yang bocor akan langsung disalahgunakan untuk menjalankan server ilegal, penambangan kripto, atau pemrosesan AI secara masif.
3. **Kerugian Finansial & Hukum:** Layanan berbasis kuota (seperti OpenAI atau AWS) akan tetap menagih biaya penggunaan ke akun Anda, yang dapat menyebabkan kerugian finansial besar hingga sanksi hukum.
4. **Pemblokiran Akun:** Penyedia layanan (Google, AWS, OpenAI, dll.) berhak memblokir akun Anda secara permanen untuk melindungi sistem mereka dari kerugian yang lebih besar.

---

### ✅ Cara yang Benar (Best Practice)

Untuk menjaga keamanan kredensial, gunakan kombinasi standar industri berikut:

1. **Berkas `.env`**: Tempat menyimpan variabel lingkungan dan data sensitif (seperti API key) secara lokal terpisah dari kode program.
2. **Berkas `.gitignore`**: Berfungsi untuk memberi tahu Git agar mengabaikan dan **tidak ikut mengunggah** berkas `.env` ke *repository* publik (seperti GitHub).
3. **Pustaka `python-dotenv`**: Digunakan di dalam kode untuk memuat variabel dari berkas `.env` ke dalam *environment variables* saat aplikasi dijalankan menggunakan fungsi `load_dotenv()`.

#### Contoh Struktur Penggunaan:

**1. Berkas `.env` (Jangan di-*commit* ke GitHub!)**
```env
OPENAI_API_KEY=sk-proj-xxxxxxxxxxxxxxxxxxxxxxxx
AWS_ACCESS_KEY_ID=AKIAIOSFODNN7EXAMPLE
```

**2. Berkas `.gitignore`**
# Abaikan file lingkungan lokal

```.gitignore
.env
__pycache__/
venv/
```

**3. Contoh Implementasi di Kode (Python) `python`**
```python
import os
from dotenv import load_dotenv

# Memuat variabel dari berkas .env
load_dotenv()

# Mengambil API key dengan aman
api_key = os.getenv("OPENAI_API_KEY")

print("API Key berhasil dimuat dengan aman!")