AI Marketing & E-Commerce Analyst

Aplikasi Streamlit berbasis AI untuk menganalisis data penjualan, transaksi, atau e-commerce secara interaktif dengan bahasa natural.
Cukup:

1. Masukkan Google AI API Key
2. Upload file CSV/Excel
3. Ajukan pertanyaan seperti:
   "Tampilkan top 10 produk berdasarkan revenue dan tren penjualan bulanan."

Aplikasi akan otomatis:
- Mendeteksi kolom penting
- Menggunakan LLM (Gemini via LangChain) untuk memahami intent
- Menampilkan grafik & insight tanpa perlu coding manual


✨ Fitur Utama

- Input Google AI API Key langsung dari sidebar (tidak disimpan di server)
- Upload CSV / XLSX / XLS
- Analisis AI berbasis LangChain + Google Gemini
- Deteksi otomatis: tanggal, revenue, quantity, kategori
- Visualisasi Top-N kategori/produk dan tren bulanan
- Antarmuka chat interaktif berbasis bahasa natural
- UI minimalis abu-abu modern


🧱 Struktur Project

ai-marketing-analyst/
├─ streamlit_app.py        # Entry point utama Streamlit
├─ ui.py                   # Custom CSS & komponen tampilan (header, chat history)
├─ data_utils.py           # Fungsi load_dataset & detect_columns
├─ llm_utils.py            # Inisialisasi LLM & fungsi decide_actions_with_llm
├─ charts.py               # Fungsi chart: Top-N & time series bulanan
├─ requirements.txt        # Dependency Python
└─ README.txt


🚀 Menjalankan Secara Lokal

1. Prasyarat:
   - Python 3.9–3.11
   - Pip

2. Clone Repository:
   git clone https://github.com/USERNAME/ai-marketing-analyst-streamlit.git
   cd ai-marketing-analyst-streamlit

3. Install Dependencies:
   pip install -r requirements.txt

   (tambahkan openpyxl jika pakai file Excel)
   pip install openpyxl

4. Jalankan Aplikasi:
   streamlit run streamlit_app.py

   Lalu buka http://localhost:8501


🔑 Google AI API Key

Aplikasi menggunakan model: gemini-2.0-flash-exp

Langkah:
1. Buka Google AI Studio
2. Buat / salin API Key
3. Masukkan di sidebar aplikasi

Catatan:
- API key tidak disimpan
- Digunakan hanya selama sesi aktif


🌐 Deploy ke Streamlit Cloud

1. Push project ke GitHub (public)
2. Buka Streamlit Community Cloud
3. Klik “New app”
4. Pilih repo, branch main, dan file: streamlit_app.py
5. Deploy

User dapat:
- Membuka URL Streamlit
- Mengisi API key
- Upload dataset
- Mulai tanya & melihat grafik


💡 Contoh Pertanyaan

- Tampilkan top 10 produk berdasarkan revenue
- Buat tren penjualan bulanan dari data ini
- Top 5 brand berdasarkan omzet
- Bandingkan performa channel berdasarkan total transaksi
- Ringkas insight utama dari data ini


🔐 Privasi & Keamanan

- Data diupload hanya untuk sesi user
- API key tidak disimpan di server
- Aman untuk demo / analisis internal

