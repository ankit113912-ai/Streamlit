#st.container() ek invisible box hai jisme tum related cheezein group karke rakh sakte ho — jaise ek card.

import streamlit as st 

with st.container(border = True)    # border true sew preety box ban jata hai 
     st.write ( " ye sbb ek box ke andar hain ")
     st.button("andar wala button ")