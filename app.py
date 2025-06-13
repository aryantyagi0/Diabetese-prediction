import streamlit as st
import pickle
import numpy as np

# Load model
model = pickle.load(open('model.pkl', 'rb'))

st.title("Diabetes Prediction App")

# Input fields
pregnancies = st.number_input('Pregnancies')
glucose = st.number_input('Glucose')
bp = st.number_input('Blood Pressure')
skin_thickness = st.number_input('Skin Thickness')
insulin = st.number_input('Insulin')
bmi = st.number_input('BMI')
dpf = st.number_input('Diabetes Pedigree Function')
age = st.number_input('Age')

if st.button('Predict'):
    features = np.array([[pregnancies, glucose, bp, skin_thickness, insulin, bmi, dpf, age]])
    result = model.predict(features)
    if result[0] == 1:
        st.error("You are likely to have diabetes 😟")
    else:
        st.success("You are unlikely to have diabetes 🙂")
