import streamlit as st

st.set_page_config(page_title="Pro Dashboard", layout="wide")

# Custom CSS
st.markdown("""
    <style>
    .stApp {
        background-color: #f5f7fa;
    }
    .stButton > button {
        background-color: #4CAF50;
        color: white;
        border-radius: 10px;
        padding: 8px 20px;
        border: none;
    }
    </style>
""", unsafe_allow_html=True)

st.title("🚀 Pro Dashboard")

col1, col2, col3 = st.columns(3)

def custom_card(title, value, color):
    st.markdown(f"""
        <div style="
            background-color: white;
            padding: 20px;
            border-radius: 15px;
            box-shadow: 0px 4px 10px rgba(0,0,0,0.1);
            text-align: center;
        ">
            <h4>{title}</h4>
            <h2 style="color:{color};">{value}</h2>
        </div>
    """, unsafe_allow_html=True)

with col1:
    custom_card("💰 Revenue", "₹1,20,000", "#4CAF50")
with col2:
    custom_card("👥 Users", "3,240", "#2196F3")
with col3:
    custom_card("⭐ Rating", "4.8", "#FF9800")

st.write("")  # Chhoti space
if st.button("📊 Report Generate Karo"):
    st.success("✅ Report ban gayi!")