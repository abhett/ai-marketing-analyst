import streamlit as st
import pandas as pd

def plot_top_n(df, metric_col, group_by_col, n: int):
    grouped = (
        df.groupby(group_by_col)[metric_col]
        .sum()
        .sort_values(ascending=False)
        .head(n)
    )
    if grouped.empty:
        st.warning("Data Top-N kosong.")
        return
    st.subheader(f"🏆 Top {n} {group_by_col} berdasarkan {metric_col}")
    st.bar_chart(grouped)

def plot_timeseries_monthly(df, metric_col, date_col):
    tmp = df.copy()
    tmp[date_col] = pd.to_datetime(tmp[date_col], errors="coerce")
    tmp = tmp.dropna(subset=[date_col])
    if tmp.empty:
        st.warning("Tidak ada data tanggal valid untuk tren.")
        return
    tmp["bulan"] = tmp[date_col].dt.to_period("M").dt.to_timestamp()
    ts = tmp.groupby("bulan")[metric_col].sum()
    if ts.empty:
        st.warning("Tidak ada data untuk tren bulanan.")
        return
    st.subheader(f"📈 Tren Penjualan Bulanan ({metric_col})")
    st.line_chart(ts)
