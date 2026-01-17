import streamlit as st
import streamlit.components.v1 as components
from supabase import create_client, Client
from datetime import datetime, timezone, timedelta
from utils import set_background_image, style_buttons  # ← 追加
import os
from dotenv import load_dotenv

load_dotenv()

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

# JSTタイムゾーンを定義
JST = timezone(timedelta(hours=9))

def go_to(page_name):
    st.session_state["page"] = page_name
    # GTMイベント送信
    components.html(f"""
    <script>
    if (typeof window.sendGTMEvent === 'function') {{
        window.sendGTMEvent('page_change', {{
            'destination_page': '{page_name}',
            'source_page': 'home'
        }});
    }}
    </script>
    """, height=0)

def home():
    set_background_image()
    style_buttons()
    st.title("Office Wing")
    st.button("購入する", key="home_btn_buy", on_click=lambda: go_to("product_list"))
    st.button("コメントする", key="home_btn_comment", on_click=lambda: go_to("comment_form"))

    st.markdown("### コメント一覧")
    res = supabase.table("message_board").select("*").order("sent_at", desc=True).limit(10).execute()
    comments = res.data
    for comment in comments:
    # UTCの文字列をdatetime型に変換
        utc_dt = datetime.fromisoformat(comment["sent_at"])
    # JSTに変換
        jst_dt = utc_dt.astimezone(JST)
    # フォーマット整形（例：2025-03-22 14:30）
        time_str = jst_dt.strftime("%Y-%m-%d %H:%M")

    # コメント表示
        st.write(f"{comment['content']} ({time_str})　by {comment['sender']}")