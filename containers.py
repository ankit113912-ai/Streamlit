#st.container() ek invisible box hai jisme tum related cheezein group karke rakh sakte ho — jaise ek card.

import streamlit as st 

with st.container(border=True):  # border=True se pretty box ban jaata hai
    st.write("Ye sab ek box ke andar hai")
    st.button("Andar wala button")



