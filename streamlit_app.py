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

<!-- Google Tag Manager (noscript) -->
<noscript><iframe src="https://www.googletagmanager.com/ns.html?id=GTM-TGJWTDM8"
height="0" width="0" style="display:none;visibility:hidden"></iframe></noscript>
<!-- End Google Tag Manager (noscript) -->

<script>
// デバッグ用：dataLayerの内容を確認
window.dataLayer = window.dataLayer || [];

// GTM読み込み確認
console.log('GTM Debug: dataLayer initialized', window.dataLayer);

// ページビューの手動送信
setTimeout(function() {
    console.log('GTM Debug: Sending page_view event');
    window.dataLayer.push({
        'event': 'page_view',
        'page_title': document.title,
        'page_location': window.location.href,
        'custom_parameter': 'streamlit_app'
    });
    console.log('GTM Debug: page_view event sent', window.dataLayer);
}, 1000);

// カスタムイベント送信関数
window.sendGTMEvent = function(eventName, parameters = {}) {
    console.log('GTM Debug: Sending custom event', eventName, parameters);
    if (typeof window !== 'undefined' && window.dataLayer) {
        window.dataLayer.push({
            'event': eventName,
            ...parameters
        });
        console.log('GTM Debug: Custom event sent', window.dataLayer);
    }
};

// GTMが正しく読み込まれているかチェック
setTimeout(function() {
    if (typeof google_tag_manager !== 'undefined') {
        console.log('GTM Debug: GTM loaded successfully');
    } else {
        console.log('GTM Debug: GTM not loaded');
    }
}, 2000);
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