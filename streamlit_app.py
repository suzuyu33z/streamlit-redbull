import streamlit as st
from dotenv import load_dotenv
import os

load_dotenv()

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