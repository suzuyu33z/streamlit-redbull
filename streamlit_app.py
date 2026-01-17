import streamlit as st
import streamlit.components.v1 as components
from dotenv import load_dotenv
import os

load_dotenv()

# --- GTM 注入 ---
components.html("""
<!-- Google Tag Manager -->
<script>
(function(w,d,s,l,i){w[l]=w[l]||[];w[l].push({'gtm.start':
new Date().getTime(),event:'gtm.js'});var f=d.getElementsByTagName(s)[0],
j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src=
'https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);
})(window,document,'script','dataLayer','GTM-TGJWTDM8');
</script>
<!-- End Google Tag Manager -->
""", height=0)

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