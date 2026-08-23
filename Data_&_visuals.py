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


