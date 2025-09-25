import streamlit as st

# Add title to your app
st.title("This is my first streamlit app created by Phalgun Kumar")

# Add some text
st.write("Welcome! This app calculates the square of a number")

st.header("Select a number")
number = st.slider("pick a number ",0,100,25)

#calculate and display the result 

st.header("Result")
st.write(f"square of number {number} is {number * number}") 