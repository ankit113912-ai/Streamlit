import streamlit as st 

st.sidebar.title("⚙️ Settings")
naam = st.sidebar.text_input("Apna naam likho")
theme = st.sidebar.selectbox("Theme chuno", ["Light", "Dark"])

st.title("Main Page")
st.write(f"Namaste, {naam}! Tumne {theme} theme chuna hai.")