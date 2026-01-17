import streamlit as st
import streamlit.components.v1 as components  # ← ★これを追加
from dotenv import load_dotenv
import os

load_dotenv()

# --- GA4 注入 ---
GA4_ID = os.getenv("GA4_MEASUREMENT_ID")

def inject_ga4(measurement_id: str):
    if not measurement_id:
        st.warning("GA4_MEASUREMENT_ID が設定されていません（.envを確認）")
        return

    components.html(
        f"""
        <script async src="https://www.googletagmanager.com/gtag/js?id={measurement_id}"></script>
        <script>
          window.dataLayer = window.dataLayer || [];
          function gtag(){{dataLayer.push(arguments);}}
          gtag('js', new Date());
          gtag('config', '{measurement_id}');
        </script>
        """,
        height=0,
    )

# ★ページを描く前に必ず1回
inject_ga4(GA4_ID)
# --- ここまで ---


from home import home
from product_list import product_list
from comment_form import comment_form

# 最初に開いたときの初期ページをhomeにする
if "page" not in st.session_state:
    st.session_state["page"] = "home"

# 現在のページ状態に応じて関数を呼び分け
page = st.session_state["page"]

if page == "home":
    home()
elif page == "product_list":
    product_list()
elif page == "comment_form":
    comment_form()