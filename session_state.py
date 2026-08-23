# Socho session state ek daayri (diary) hai jisme app apni values likh kar rakhta hai, taaki re-run hone ke baad bhi bhoole na.

import streamlit as st

# Pehli baar agar "count" naam ki cheez daayri mein nahi hai, to bana do (0 se)
if "count" not in st.session_state:
    st.session_state.count = 0

# Button dabane par daayri mein value badhao
if st.button("Badhao"):
    st.session_state.count += 1

st.write("Counter:", st.session_state.count)