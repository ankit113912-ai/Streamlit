# Mini Dashboard 

import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

st.set_page_config(page_title="Data Dashboard", layout="wide")
st.title("📊 Mera Data Dashboard")

# Metrics
col1, col2, col3 = st.columns(3)
col1.metric("Total Sales", "₹1,20,000", "8%")
col2.metric("Users", "3,240", "12%")
col3.metric("Rating", "4.6 ⭐", "-0.1")

st.divider()  # Ek line khinch deta hai, sections alag karne ke liye

# Data
data = pd.DataFrame({
    "Month": ["Jan", "Feb", "Mar", "Apr"],
    "Sales": [100, 150, 130, 200]
})

col1, col2 = st.columns(2)
with col1:
    st.subheader("Table View")
    st.dataframe(data, use_container_width=True)

with col2:
    st.subheader("Chart View")
    fig = px.line(data, x="Month", y="Sales", markers=True)
    st.plotly_chart(fig, use_container_width=True)


                    






 # Graphs Charts ( Streamlit mai built - in simple charts hote hian )
import streamlit as st 
import pandas as pd 
import numpy as pd 



# Make a random data for chart :- 

chart_data = pd.DataFrame(
    np.random.randn(20,3),
    columns = ["Sales", "Profit", "Cost"]
)

st.subheader("Line Chart ")
st.line_chart(chart_data)

st.subheader("📊 Bar Chart")
st.bar_chart(chart_data)

st.subheader("📉 Area Chart")
st.area_chart(chart_data)




# plotly 


import plotly.express as px

fig = px.bar(data, x="Naam", y="Age", color="City", title="Age by City")
st.plotly_chart(fig, use_container_width=True)