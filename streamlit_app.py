import streamlit as st
import pandas as pd

from ui import apply_custom_css, render_header, show_chat_history
from data_utils import load_dataset, detect_columns
from llm_utils import init_llm, decide_actions_with_llm
from charts import plot_top_n, plot_timeseries_monthly

# =========================
# 1. PAGE CONFIG
# =========================
st.set_page_config(
    page_title="📊 AI Marketing & E-Commerce Analyst",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =========================
# CUSTOM CSS + HEADER
# =========================
apply_custom_css()
render_header()

# =========================
# 2. INIT SESSION STATE
# =========================
if "df" not in st.session_state:
    st.session_state.df = None
if "colmap" not in st.session_state:
    st.session_state.colmap = {}
if "messages" not in st.session_state:
    st.session_state.messages = []

# =========================
# 3. SIDEBAR: API KEY + UPLOAD + RESET
# =========================
with st.sidebar:
    st.subheader("🔐 Google AI API Key")
    google_api_key = st.text_input(
        "Masukkan Google AI API Key",
        type="password",
        help="Ambil dari Google AI Studio lalu tempel di sini. Kunci ini hanya dipakai di sesi Anda."
    )

    st.subheader("📂 Upload Dataset")
    uploaded_file = st.file_uploader(
        "Pilih file CSV / Excel",
        type=["csv", "xlsx", "xls"],
        help="Misalnya: data transaksi, order, penjualan e-commerce."
    )

    if st.button("🔄 Reset Chat (data tetap)"):
        st.session_state.messages = []
        st.rerun()

if not google_api_key:
    st.info("Please add your Google AI API key in the sidebar to start chatting.", icon="🗝️")
    st.stop()

# =========================
# 4. LOAD DATASET & DETECT COLUMNS
# =========================
if uploaded_file is not None:
    try:
        df = load_dataset(uploaded_file)
        st.session_state.df = df
        st.session_state.colmap = detect_columns(df)
        st.success(f"✅ Dataset dimuat: {df.shape[0]} baris, {df.shape[1]} kolom.")
    except Exception as e:
        st.error(f"❌ Gagal membaca file: {e}")
        st.stop()

if st.session_state.df is None:
    st.info("📂 Silakan upload file CSV/Excel untuk mulai analisis.", icon="ℹ️")
    st.stop()

df = st.session_state.df
colmap = st.session_state.colmap

with st.expander("🔎 Deteksi Otomatis Kolom Penting"):
    st.write(f"- Kolom tanggal   : `{colmap.get('date_col')}`")
    st.write(f"- Kolom revenue   : `{colmap.get('metric_col')}`")
    st.write(f"- Kolom quantity  : `{colmap.get('qty_col')}`")
    st.write(f"- Kolom kategori  : `{colmap.get('category_col')}`")
    st.caption("Jika tidak tepat, tulis nama kolom yang benar dalam pertanyaan (misal: 'pakai kolom Total').")

# =========================
# 5. VALIDASI API KEY
# =========================
if not google_api_key:
    st.warning("Masukkan Google AI API Key di sidebar untuk mengaktifkan analisis AI.", icon="🗝️")
    st.stop()

# =========================
# 6. INISIALISASI LLM
# =========================
llm = init_llm(google_api_key)

# =========================
# 10. TAMPILKAN RIWAYAT CHAT
# =========================
show_chat_history()

# =========================
# 11. INPUT CHAT + EKSEKUSI AKSI
# =========================
user_query = st.chat_input(
    "Contoh: 'Tampilkan top 10 produk berdasarkan revenue dan tren penjualan bulanannya'"
)

if user_query:
    st.session_state.messages.append({"role": "user", "content": user_query})
    with st.chat_message("user"):
        st.markdown(user_query)

    actions = decide_actions_with_llm(llm, user_query, df, colmap)
    full_explanation_parts = []

    with st.chat_message("assistant"):
        for act in actions:
            atype = (act.get("type") or "").lower()
            metric = act.get("metric_column") or colmap.get("metric_col")
            group = act.get("group_by") or colmap.get("category_col")
            date = act.get("date_column") or colmap.get("date_col")
            n = int(act.get("n") or 10)
            expl = (act.get("explanation") or "").strip()

            if atype == "top_n" and metric in df.columns and group in df.columns:
                plot_top_n(df, metric, group, n)
                full_explanation_parts.append(
                    expl or f"Berikut Top {n} {group} berdasarkan {metric}."
                )

            elif atype == "timeseries" and metric in df.columns and date in df.columns:
                plot_timeseries_monthly(df, metric, date)
                full_explanation_parts.append(
                    expl or f"Berikut tren penjualan bulanan berdasarkan {metric} dan {date}."
                )

            elif atype == "summary":
                full_explanation_parts.append(
                    expl or "Berikut ringkasan insight dari data Anda."
                )

        if not full_explanation_parts:
            st.markdown(
                "Saya kesulitan mengenali kolom yang dimaksud. "
                "Coba tulis: `Top 10 produk berdasarkan kolom Total dan grup Jenis Produk`."
            )
        else:
            st.markdown("**Insight:**")
            st.markdown("\n\n".join(full_explanation_parts))

    st.session_state.messages.append({
        "role": "assistant",
        "content": "\n\n".join(full_explanation_parts) if full_explanation_parts else "(lihat grafik di atas)"
    })
