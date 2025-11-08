import pandas as pd

def load_dataset(file) -> pd.DataFrame:
    """Baca CSV/Excel dengan auto-deteksi delimiter untuk CSV."""
    if file.name.lower().endswith(".csv"):
        sample = file.read(4096).decode("utf-8", errors="ignore")
        file.seek(0)
        sep = ";" if sample.count(";") > sample.count(",") else ","
        return pd.read_csv(file, sep=sep)
    return pd.read_excel(file)

def detect_columns(df: pd.DataFrame) -> dict:
    """Deteksi otomatis kolom tanggal, revenue, qty, kategori."""
    cols = list(df.columns)
    lower = [c.lower() for c in cols]

    def find(candidates, numeric=False, date=False):
        for c, lc in zip(cols, lower):
            if any(k in lc for k in candidates):
                if numeric and not pd.api.types.is_numeric_dtype(df[c]):
                    continue
                if date:
                    try:
                        pd.to_datetime(df[c], errors="raise")
                    except Exception:
                        continue
                return c
        return None

    return {
        "date_col": find(["date", "tanggal", "order_date", "trx_date"], date=True),
        "metric_col": find(
            ["revenue", "amount", "total", "gmv", "sales", "pendapatan", "omzet"],
            numeric=True
        ),
        "qty_col": find(["qty", "quantity", "jumlah", "pcs", "unit"], numeric=True),
        "category_col": find(
            ["product", "produk", "item", "sku", "category", "kategori", "brand", "campaign", "channel"]
        ),
    }
