import streamlit as st 
import pandas as pd 


# A small fake  data table create :- 
data = pd.DataFrame({
    "Naam": ["Amit", "Riya", "Karan", "Sneha"],
    "Age": [25, 30, 22, 28],
    "City": ["Delhi", "Mumbai", "Pune", "Chennai"]
})



# How to show a Data Frams :- 

st.subheader("All Data Table ")
st.dataframe(data)                  # interactive table - short , search karte hai 


st.subheader("Simple Table ")
st.table(data)                     # Static Table - simple dhikata hai , interactive nahi 


""" st.dataframe() → Interactive (sort/scroll kar sakte ho) — isko zyada use karo
    st.table() → Simple, static — chhoti tables ke liye"""



# How to highlight a  Numbers - Metrix :- 

col1, col2, col3 = st.columns(3)
col1.metric(label="Total Users", value="1,234", delta="12%")
col2.metric(label="Sales", value="₹45,000", delta="-5%")
col3.metric(label="Rating", value="4.8 ⭐", delta="0.2")

