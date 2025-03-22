import streamlit as st

def set_background_image():
    st.markdown(
        """
        <style>
        .stApp {
            background-image: url("https://xdpyenbkvrzimpuwzkcc.supabase.co/storage/v1/object/public/product-images//redbullback.png");
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

def style_buttons():
    st.markdown("""
        <style>
        /* 通常ボタン */
        div.stButton > button {
            background-color: #0066cc;
            color: white;
            border: none;
            padding: 0.5em 1em;
            border-radius: 8px;
            font-weight: bold;
            transition: background-color 0.3s;
        }
        </style>
    """, unsafe_allow_html=True)
