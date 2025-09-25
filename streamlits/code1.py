import streamlit as st
import pandas as pd
import numpy as np

# Add Title and Description

st.title("My First streamlit app")
st.write("This is a simple app to demonstrate basic functionalities of streamlits")

st.sidebar.header("User input features")

# Text input

name = st.sidebar.text_input("What is your name?", "Streamlit User")

# Slider

age = st.sidebar.slider("what is your age",0,100,20)

# Select box

color = st.sidebar.selectbox("Choose the color", ["Blue","Green","Red","Purple"])

# Display content on page

st.header(f"Welcome {name}")
st.write(f"Your age is {age} and your favorite color is {color}")

st.subheader("Here is some random data")

df = pd.DataFrame({"Name":['Ramesh','Suresh'], "Age": [25,35]})

st.dataframe(df)

rawDataFlag = st.checkbox("Show raw data")

if rawDataFlag:
    st.dataframe(df)

showImage = st.checkbox("Show image")
if showImage:
    st.image(r"C:\Users\Kumar\OneDrive\Desktop\horse.jpg")
