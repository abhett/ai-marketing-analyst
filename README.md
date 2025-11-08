AI Marketing & E-Commerce Analyst

Aplikasi Streamlit berbasis AI untuk menganalisis data penjualan, transaksi, atau e-commerce secara interaktif dengan bahasa natural.
Cukup:

Masukkan Google AI API Key

Upload file CSV/Excel

Ajukan pertanyaan seperti:

"Tampilkan top 10 produk berdasarkan revenue dan tren penjualan bulanan."

Aplikasi akan otomatis:

Mendeteksi kolom penting

Menggunakan LLM (Gemini via LangChain) untuk memahami intent

Menampilkan grafik & insight tanpa perlu coding manual

✨ Fitur Utama

🔐 Input Google AI API Key langsung dari sidebar (tidak disimpan di server)

📂 Upload CSV / XLSX / XLS

🤖 Analisis AI berbasis LangChain + Google Gemini

🔍 Deteksi otomatis:

Kolom tanggal

Kolom revenue/total

Kolom quantity

Kolom kategori/produk/brand/channel

🏆 Visualisasi:

Top-N kategori/produk berdasarkan metrik tertentu

Tren penjualan bulanan (timeseries)

💬 Antarmuka chat:

Tanyakan dengan bahasa natural

Response berupa grafik + ringkasan insight

🎨 UI minimalis abu-abu modern (custom CSS)

🧱 Arsitektur & Struktur Project
ai-marketing-analyst/
├─ streamlit_app.py        # Entry point utama Streamlit
├─ ui.py                   # Custom CSS & komponen tampilan (header, chat history)
├─ data_utils.py           # Fungsi load_dataset & detect_columns
├─ llm_utils.py            # Inisialisasi LLM & fungsi decide_actions_with_llm
├─ charts.py               # Fungsi chart: Top-N & time series bulanan
├─ requirements.txt        # Dependency Python
└─ README.md


Semua logika asli dipertahankan, hanya dipisah menjadi modul agar:

Lebih rapi

Mudah di-maintain

Siap untuk deployment production/demo

🚀 Menjalankan Secara Lokal
1. Prasyarat

Python 3.9–3.11

Pip

2. Clone Repository
git clone https://github.com/USERNAME/ai-marketing-analyst-streamlit.git
cd ai-marketing-analyst-streamlit

3. Install Dependencies
pip install -r requirements.txt


Jika menggunakan file Excel:

pip install openpyxl

4. Jalankan Aplikasi
streamlit run streamlit_app.py


Lalu buka URL yang muncul (biasanya http://localhost:8501).

🔑 Konfigurasi Google AI API Key

Aplikasi menggunakan ChatGoogleGenerativeAI (LangChain) dengan model:

gemini-2.0-flash-exp

Langkah:

Buka Google AI Studio

Buat / salin API Key

Di aplikasi Streamlit:

Buka sidebar

Tempel API key di field "Masukkan Google AI API Key"

API key:

Hanya digunakan di sisi aplikasi untuk sesi Anda

Tidak disimpan di repo

Tidak dikodekan hard-coded

🌐 Deploy ke Streamlit Community Cloud

Push project ini ke GitHub (public).

Buka Streamlit Community Cloud.

Klik "New app".

Pilih:

Repository: repo yang berisi project ini

Branch: main

File: streamlit_app.py

Deploy.

Pengguna akhir:

Mengakses URL Streamlit

Mengisi API key mereka

Upload dataset mereka

Mulai tanya jawab & melihat grafik analisis

💡 Contoh Pertanyaan yang Didukung

Tampilkan top 10 produk berdasarkan revenue

Buat tren penjualan bulanan dari data ini

Top 5 brand berdasarkan omzet

Bandingkan performa channel berdasarkan total transaksi

Ringkas insight utama dari data ini

Aplikasi akan mengubah pertanyaan menjadi aksi terstruktur:

top_n

timeseries

summary

Lalu menjalankan visualisasi sesuai struktur tersebut.

🔐 Privasi & Keamanan

Data yang diupload hanya diproses di sesi aplikasi.

API key dimasukkan oleh user sendiri via sidebar.

Tidak ada API key disimpan di dalam repo GitHub.

Cocok untuk demo, PoC, atau analisis internal.
