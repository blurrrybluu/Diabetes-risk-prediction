# app.py
import streamlit as st
import joblib
import pandas as pd
import os

# Debug: Check if files exist
st.write("Looking for model files...")
if not os.path.exists("diabetes_model.pkl"):
    st.error("diabetes_model.pkl NOT FOUND! Run CELL 13 first.")
    st.stop()
if not os.path.exists("model_columns.pkl"):
    st.error("model_columns.pkl NOT FOUND! Run CELL 13 first.")
    st.stop()

# Load model
model = joblib.load("diabetes_model.pkl")
cols = joblib.load("model_columns.pkl")

st.title("Diabetes Risk Predictor")
st.write("Adjust sliders to see live risk prediction")

# Input sliders
preg = st.slider("Pregnancies", 0, 17, 1)
gluc = st.slider("Glucose", 0, 200, 120)
bp = st.slider("Blood Pressure", 0, 122, 70)
skin = st.slider("Skin Thickness", 0, 99, 30)
ins = st.slider("Insulin", 0, 846, 0)
bmi = st.slider("BMI", 0.0, 70.0, 25.0)
dpf = st.slider("Diabetes Pedigree", 0.0, 2.5, 0.5)
age = st.slider("Age", 21, 100, 30)

# BMI Category
bmi_cat = "Obese" if bmi >= 30 else "Overweight" if bmi >= 25 else "Normal" if bmi >= 18.5 else "Underweight"

data = {
    "Pregnancies": preg, "Glucose": gluc, "BloodPressure": bp,
    "SkinThickness": skin, "Insulin": ins, "BMI": bmi,
    "DiabetesPedigreeFunction": dpf, "Age": age,
    "BMI_Category_Normal": int(bmi_cat == "Normal"),
    "BMI_Category_Obese": int(bmi_cat == "Obese"),
    "BMI_Category_Overweight": int(bmi_cat == "Overweight"),
    "BMI_Category_Underweight": int(bmi_cat == "Underweight")
}

if st.button("Predict Risk"):
    X = pd.DataFrame([data])[cols]
    prob = model.predict_proba(X)[0][1]
    st.metric("Diabetes Risk", f"{prob:.1%}")
    
    if prob > 0.5:
        st.error("HIGH RISK – Consult a doctor!")
    else:
        st.success("LOW RISK – Keep healthy!")