import streamlit as st
from supabase import create_client, Client
from datetime import datetime
from utils import set_background_image, style_buttons
import os
from dotenv import load_dotenv

load_dotenv()

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

def comment_form():
    set_background_image()
    style_buttons()
    st.title("コメントフォーム")

    # 入力欄
    sender = st.text_input("ペンネーム")
    comment = st.text_area("コメント")

    # 送信処理
    if st.button("送信"):
        if sender and comment:
            supabase.table("message_board").insert({
                "sender": sender,
                "content": comment,
                "sent_at": datetime.utcnow().isoformat()  # UTCのままでOK
            }).execute()
            st.success("コメントを送信しました！")
            st.session_state["page"] = "home"
        else:
            st.warning("ペンネームとコメントを両方入力してください。")

    # 戻るボタン
    st.button("← 戻る", on_click=lambda: st.session_state.update({"page": "home"}))
