# app.py
import streamlit as st
import requests
import pandas as pd

st.title("Sleep Quality Predictor")

# Input fields
gender = st.selectbox("Gender", ["Male", "Female"])
age = st.number_input("Age", min_value=29, max_value=59, value=30)
occupation = st.text_input("Occupation", "Engineer")
sleep_duration = st.number_input("Sleep Duration (hrs)", min_value=0.0, max_value=10.0, value=7.5)
physical_activity_level = st.number_input("Physical Activity (hrs)", 0, 100, 50)
stress_level = st.number_input("Stress Level (0:Excellent 10:Terrible)", 0, 10, 4)
bmi_category = st.selectbox("BMI Category", ["Normal", "Overweight", "Obese"])
heart_rate = st.number_input("Heart Rate", 30, 200, 70)
daily_steps = st.number_input("Daily Steps", 0, 50000, 6000)
sleep_disorder = st.selectbox("Sleep Disorder", ["None", "Insomnia", "Sleep Apnea"])
systolic = st.number_input("Systolic BP", 80, 200, 120)
diastolic = st.number_input("Diastolic BP", 40, 150, 80)

if st.button("Predict"):
    data = {
        "gender": gender,
        "age": age,
        "occupation": occupation,
        "sleep_duration": sleep_duration,
        "physical_activity_level": physical_activity_level,
        "stress_level": stress_level,
        "bmi_category": bmi_category,
        "heart_rate": heart_rate,
        "daily_steps": daily_steps,
        "sleep_disorder": sleep_disorder,
        "systolic": systolic,
        "diastolic": diastolic
    }

    response = requests.post("http://localhost:9696/predict", json=data)
    if response.status_code == 200:
        result = response.json()
        st.success(f"Predicted Sleep Quality: {result['sleep_quality']}")
        st.info(f"Predicted Value: {result['sleep_prediction']:.2f}")
    else:
        st.error("Prediction failed!")
