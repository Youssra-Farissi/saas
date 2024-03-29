import streamlit as st
st.set_page_config(
    page_title = "Hello",
    page_icon= ""
)

expander = st.expander("Domain knowledge of Oil & Gas")

expander.write("""
Hello World!""")