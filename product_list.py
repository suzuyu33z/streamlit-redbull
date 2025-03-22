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

def go_to(page_name):
    st.session_state["page"] = page_name

def product_list():
    set_background_image()
    style_buttons()
    st.title("商品一覧")

    # 商品データを取得
    res = supabase.table("product_master").select("*").execute()
    products = res.data

    # 支払いURL（今回は1件固定でOK）
    pay_res = supabase.table("payment_info").select("paypay_url").limit(1).execute()
    pay_url = pay_res.data[0]["paypay_url"] if pay_res.data else None

    # 商品を1つずつ表示
    for product in products:
        with st.container():
            cols = st.columns([1, 2])  # 左：画像、右：テキスト
            with cols[0]:
                st.image(product["image_url"], width=120)
            with cols[1]:
                st.subheader(product["name"])
                st.write(product["description"])
                st.markdown(f"価格: **{product['price']} 円**")

                # ボタン押したら購入処理＋遷移
                if st.button("購入へ進む（PayPayで支払い）", key=product["id"]):
                    # ①購入履歴をUTCで記録（Supabaseの推奨通り）
                    now_utc = datetime.utcnow().isoformat()
                    supabase.table("purchase_info").insert({
                        "product_id": product["id"],
                        "purchased_at": now_utc
                    }).execute()

                    # ②支払いリンクに遷移（※Streamlitのリンクボタンで対応）
                    st.markdown(f"""
                        <meta http-equiv="refresh" content="0;URL='{pay_url}'" />
                    """, unsafe_allow_html=True)

        st.markdown("---")  # 区切り線

    # 戻るボタン
    st.button("← 戻る", on_click=lambda: go_to("home"))