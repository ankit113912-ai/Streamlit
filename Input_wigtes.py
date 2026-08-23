import streamlit as st 


# 1.  Button 

if st.button ( " mujhe click karo "):
    st.write("wahh! tumne click kiya ")


# 2. Text Input 

if st.text_input( "Apna naam likho ") : 
    st.write ("Namaste :","naam")


# 3. Slider 

age = st.slider("Apni age chuno", 0, 100, 25)
st.write("Tumhari age hai:", age)


# 4. Checkbok 

if st.checkbox ( " kya tumhe python pasand hai ?") : 
    st.write ( "yes ! python sabse powerful hai ")


# 5. Radio Button ( Chose a one option )

pasand =  st.radio ( "Tumahari favourite chije ?", ["cricket","coding","gaming"])
st.write ("Tumne chuna:", pasand)


# 6. Selectbox (dropdown)
city = st.selectbox("Apna sheher chuno", ["Delhi", "Mumbai", "Bangalore"])
st.write("Sheher:", city)