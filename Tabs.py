
#   Tabs - Ek screen multiple pages jaisa Feel 

import streamlit as st 


""" socho tumhare paas 3 alag sections hain (jaise "Home", "About", "Contact") lekin
 tum unhe ek hi page pe tabs mein dikhana chahte ho:   """

tab1, tab2 ,tab3 = st.tabs (["Home" , "Data" , "setting"])

with tab1 :
    st.write ("This is a Home  tab ")

with tab2 : 
    st.write ("This is a Data tab ")

with tab3 : 
    st.write ("This is a setting tab ")