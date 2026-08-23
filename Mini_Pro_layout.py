import streamlit as st 

st.set_page_config(page_title= " Agentra", layout="wide")             # Poori screen use karo 


# SIDEBAR

st.sidebar.title("Menu")
page_colour = st.sidebar.radio("Nagavigate karo", ["Dashboard", "Profile"])


# Main Area

st.title ("Agentra  🚀")

col1,col2 = st.columns(2)
with col1 : 
    with st.container(border=True): 
        st.subheader("status")
        st.write ( " here's show data ")

with col2 : 
    with st.container(border=True):
        st.subheader("info")
        st.write ( " here's show info ")


tab1 , tab2  = st.tabs (["Overview","Details"])

with tab1 : 
    st.write ( " content of Overview ")

with tab2 : 
    st.write ( " content of Details ")


with st.expander("More Explor ?") :

    st.write ( " Extra content are here ")

    