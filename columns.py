import streamlit as st 

col1,col2,col3 = st.columns(3)       # Teen barabar hisso mai bantt do 

with col1:
    st.header("column 1 ")
    st.write ("ye phela box hai ")


with col2:
    st.header("column 2")
    st.write ("ye dusra box hai ")

with col3:
    st.header("column 3")
    st.write ("ye tesraa box hai ")


