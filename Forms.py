import streamlit as st

with st.form("mera_form"):
    naam = st.text_input("Naam")
    age = st.slider("Age", 0, 100)
    submit = st.form_submit_button("Submit Karo")

    if submit:
        st.write(f"Naam: {naam}, Age: {age}")