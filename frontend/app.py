import streamlit as st
import requests

st.title("AESI MRP Pilot")

if st.button("Check System"):
    try:
        r = requests.get("http://localhost:8000")
        st.write(r.json())
    except Exception as e:
        st.error(f"Backend not running: {e}")
