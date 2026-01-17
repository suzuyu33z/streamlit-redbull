import streamlit as st
import streamlit.components.v1 as components
from dotenv import load_dotenv
import os

load_dotenv()

# --- GA4 直接実装 ---
ga4_measurement_id = os.getenv("GA4_MEASUREMENT_ID", "G-7D1HYY5YN7")

components.html(f"""
<!-- Global site tag (gtag.js) - Google Analytics -->
<script async src="https://www.googletagmanager.com/gtag/js?id={ga4_measurement_id}"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){{dataLayer.push(arguments);}}
  gtag('js', new Date());
  gtag('config', '{ga4_measurement_id}', {{
    'page_title': document.title,
    'page_location': window.location.href,
    'custom_parameter': 'streamlit_app'
  }});
  
  // デバッグ用
  console.log('GA4 Debug: Analytics initialized with ID: {ga4_measurement_id}');
  console.log('GA4 Debug: Page view sent');
  
  // カスタムイベント送信関数
  window.sendGA4Event = function(eventName, parameters) {{
    parameters = parameters || {{}};
    console.log('GA4 Debug: Sending custom event', eventName, parameters);
    gtag('event', eventName, parameters);
  }};
</script>
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