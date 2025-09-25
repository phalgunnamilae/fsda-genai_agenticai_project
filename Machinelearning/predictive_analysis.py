import streamlit as st
import pickle
import numpy as np 

model = pickle.load(open(r"C:\Users\Kumar\linear_regression_model.pkl",'rb'))

st.title("Salary Prediction App")

st.write("This app predicts the salary of the employees based on the experience")

years_exp = st.number_input("Enter the years of Exp", min_value=0.0, max_value=50.0, value = 1.0, step = 0.5)

if(st.button("Predict Salary")):
    experience_input = np.array([[years_exp]])
    prediction = model.predict(experience_input)
    
    #display result
    st.success(f"Predicted salary for the given years of exp {experience_input[0][0]} is ${prediction[0]:,.2f}")

st.write(f"The model is trained using the data of the salaries and the years of experience data")