import json
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage

def init_llm(google_api_key: str):
    return ChatGoogleGenerativeAI(
        model="gemini-2.0-flash-exp",
        google_api_key=google_api_key,
        temperature=0.2,
    )

def extract_json(text: str) -> str | None:
    """Ambil blok JSON { ... } dari teks (handle ```json ...``` dan teks campur)."""
    text = text.strip()

    if "```" in text:
        parts = text.split("```")
        for part in parts:
            part = part.strip()
            if not part:
                continue
            if part.lower().startswith("json"):
                part = part[4:].strip()
            if part.startswith("{") and part.endswith("}"):
                return part

    start = text.find("{")
    end = text.rfind("}")
    if start != -1 and end != -1 and end > start:
        candidate = text[start:end+1].strip()
        if candidate.startswith("{") and candidate.endswith("}"):
            return candidate

    return None

def decide_actions(user_query: str, df, colmap: dict):
    schema_hint = {
        "actions": [
            {
                "type": "top_n / timeseries / summary",
                "metric_column": "nama kolom angka (misal: Total)",
                "group_by": "nama kolom kategori (misal: Jenis Produk)",
                "date_column": "nama kolom tanggal (misal: Tanggal)",
                "n": "jumlah top N (untuk top_n)",
                "explanation": "penjelasan singkat dalam bahasa Indonesia"
            }
        ]
    }

    prompt = f"""
Kamu adalah AI analis data marketing.

User bertanya:
\"\"\"{user_query}\"\"\"


Kolom tersedia:
{list(df.columns)}

Deteksi otomatis:
{json.dumps(colmap, ensure_ascii=False)}

Tugasmu:
- Kembalikan daftar aksi dalam format JSON **valid** (tanpa teks lain) dengan schema:
{json.dumps(schema_hint, indent=2)}

Aturan:
- Jika user minta "top 10 produk berdasarkan revenue" → 1 aksi type="top_n".
- Jika user minta "tren penjualan harian/bulanan" → 1 aksi type="timeseries".
- Jika minta keduanya → 2 aksi (top_n + timeseries).
- Gunakan kolom paling cocok (boleh pakai deteksi otomatis).
- Jangan keluarkan penjelasan di luar JSON.
"""

    llm = ChatGoogleGenerativeAI(
        model="gemini-2.0-flash-exp",
        google_api_key=df._google_api_key if hasattr(df, "_google_api_key") else None,
        temperature=0.2,
    )

    # NOTE:
    # Jika tidak ingin trik di atas, di streamlit_app kita langsung panggil llm.invoke()
    # dengan instance yang dibuat di sana (lebih eksplisit). Untuk patuh ke "jangan ubah logika",
    # sebaiknya di main file yang memegang llm. Lihat streamlit_app.py di bawah.
    # Di sini saya tuliskan versi generik, tapi di implementasi final kita TIDAK pakai llm lokal ini.
    # Di streamlit_app decide_actions dipanggil dengan llm yang di-pass dari luar.

    # Versi final yang dipakai: fungsi di bawah (silakan gunakan ini di streamlit_app):

def decide_actions_with_llm(llm, user_query: str, df, colmap: dict):
    schema_hint = {
        "actions": [
            {
                "type": "top_n / timeseries / summary",
                "metric_column": "nama kolom angka (misal: Total)",
                "group_by": "nama kolom kategori (misal: Jenis Produk)",
                "date_column": "nama kolom tanggal (misal: Tanggal)",
                "n": "jumlah top N (untuk top_n)",
                "explanation": "penjelasan singkat dalam bahasa Indonesia"
            }
        ]
    }

    prompt = f"""
Kamu adalah AI analis data marketing.

User bertanya:
\"\"\"{user_query}\"\"\"


Kolom tersedia:
{list(df.columns)}

Deteksi otomatis:
{json.dumps(colmap, ensure_ascii=False)}

Tugasmu:
- Kembalikan daftar aksi dalam format JSON **valid** (tanpa teks lain) dengan schema:
{json.dumps(schema_hint, indent=2)}

Aturan:
- Jika user minta "top 10 produk berdasarkan revenue" → 1 aksi type="top_n".
- Jika user minta "tren penjualan harian/bulanan" → 1 aksi type="timeseries".
- Jika minta keduanya → 2 aksi (top_n + timeseries).
- Gunakan kolom paling cocok (boleh pakai deteksi otomatis).
- Jangan keluarkan penjelasan di luar JSON.
"""

    res = llm.invoke([HumanMessage(content=prompt)])
    raw = res.content.strip()

    json_str = extract_json(raw)
    if not json_str:
        return [{
            "type": "summary",
            "metric_column": colmap.get("metric_col"),
            "group_by": colmap.get("category_col"),
            "date_column": colmap.get("date_col"),
            "n": 10,
            "explanation": "Berikut ringkasan insight dari data berdasarkan permintaan Anda."
        }]

    try:
        data = json.loads(json_str)
        actions = data.get("actions", [])
        if not isinstance(actions, list) or not actions:
            raise ValueError("No valid actions key")
        return actions
    except Exception:
        return [{
            "type": "summary",
            "metric_column": colmap.get("metric_col"),
            "group_by": colmap.get("category_col"),
            "date_column": colmap.get("date_col"),
            "n": 10,
            "explanation": "Berikut ringkasan insight dari data berdasarkan permintaan Anda."
        }]
