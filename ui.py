import streamlit as st

def apply_custom_css():
    st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600&display=swap');
        .stApp { background-color: #f5f5f5; font-family: 'Inter', sans-serif; }
        [data-testid="stSidebar"] { background-color: #e8e8e8; border-right: 1px solid #d0d0d0; }
        [data-testid="stSidebar"] .stMarkdown { color: #4a4a4a; }
        .main .block-container { padding-top: 2rem; padding-bottom: 2rem; background-color: #fafafa; }
        h1, h2, h3 { color: #3a3a3a !important; font-weight: 500 !important; letter-spacing: -0.5px; }
        h1 { font-size: 2rem !important; margin-bottom: 0.5rem !important; }
        p, .stMarkdown, .stText { color: #5a5a5a; font-weight: 300; }
        .stCaption { color: #8a8a8a !important; font-size: 0.85rem !important; }
        .stButton > button {
            background-color: #7a7a7a; color: white; border: none; border-radius: 6px;
            padding: 0.5rem 1.5rem; font-weight: 400; transition: all 0.3s ease;
            box-shadow: 0 1px 3px rgba(0,0,0,0.1);
        }
        .stButton > button:hover {
            background-color: #5a5a5a; box-shadow: 0 2px 6px rgba(0,0,0,0.15);
            transform: translateY(-1px);
        }
        .stTextInput > div > div > input,
        .stFileUploader {
            background-color: white; border: 1px solid #d0d0d0; border-radius: 6px;
            color: #4a4a4a; font-family: 'Inter', sans-serif;
        }
        .stTextInput > div > div > input:focus {
            border-color: #9a9a9a; box-shadow: 0 0 0 1px #9a9a9a;
        }
        .stChatMessage {
            background-color: white; border: 1px solid #e0e0e0; border-radius: 8px;
            padding: 1rem; margin-bottom: 0.75rem;
            box-shadow: 0 1px 2px rgba(0,0,0,0.05);
        }
        .streamlit-expanderHeader {
            background-color: white; border: 1px solid #e0e0e0; border-radius: 6px;
            color: #4a4a4a; font-weight: 400;
        }
        .streamlit-expanderContent {
            background-color: #fcfcfc; border: 1px solid #e0e0e0; border-top: none;
            border-radius: 0 0 6px 6px;
        }
        .stInfo, .stWarning, .stSuccess {
            background-color: white; border-left: 4px solid #9a9a9a; border-radius: 4px; color: #4a4a4a;
        }
        .stSuccess { border-left-color: #7a7a7a; }
        .stPlotlyChart, .stVegaLiteChart {
            background-color: white; border-radius: 8px; padding: 1rem;
            box-shadow: 0 1px 3px rgba(0,0,0,0.08);
        }
        .stSubheader {
            color: #4a4a4a !important; font-weight: 500 !important; margin-top: 1rem;
        }
        hr { border-color: #d5d5d5; margin: 2rem 0; }
        code {
            background-color: #e8e8e8; color: #4a4a4a;
            padding: 0.2rem 0.4rem; border-radius: 3px; font-size: 0.9em;
        }
        [data-testid="stFileUploader"] {
            background-color: white; border: 2px dashed #c0c0c0; border-radius: 8px; padding: 1rem;
        }
        .stChatInput > div {
            background-color: white; border: 1px solid #d0d0d0; border-radius: 8px;
        }
    </style>
    """, unsafe_allow_html=True)

def render_header():
    st.title("📊 AI Marketing & E-Commerce Analyst")
    st.caption(
        "1️⃣ Masukkan Google AI API Key di sidebar · "
        "2️⃣ Upload CSV/Excel · "
        "3️⃣ Tanya pakai bahasa natural → grafik & insight otomatis."
    )

def show_chat_history():
    st.markdown("---")
    st.subheader("💬 Chat Analisis")
    for m in st.session_state.messages:
        with st.chat_message(m["role"]):
            st.markdown(m["content"])
