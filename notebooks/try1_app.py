# app.py
import streamlit as st
import requests

# Page setup
st.set_page_config(page_title="😴 Sleep Quality Predictor", layout="wide")

# Header section with emoji and image
st.title("😴 Sleep Quality Predictor")
st.markdown("### 💤 Understand how your daily habits affect your sleep quality!")

st.image(
    "https://cdn-icons-png.flaticon.com/512/616/616408.png",
    width=120,
    caption="Predict your sleep quality instantly"
)

st.markdown("---")

# Split layout into columns for better readability
col1, col2, col3 = st.columns(3)

with col1:
    gender = st.selectbox("👩‍🦰 Gender", ["Male", "Female"])
    age = st.number_input("🎂 Age", min_value=18, max_value=100, value=30)
    occupation = st.text_input("💼 Occupation", "Engineer")
    bmi_category = st.selectbox("⚖️ BMI Category", ["Normal", "Overweight", "Obese"])
    sleep_disorder = st.selectbox("😵 Sleep Disorder", ["None", "Insomnia", "Sleep Apnea"])

with col2:
    sleep_duration = st.number_input("🕒 Sleep Duration (hrs)", min_value=0.0, max_value=12.0, value=7.5)
    physical_activity_level = st.slider("🏃 Physical Activity Level", 0, 100, 50)
    stress_level = st.slider("😫 Stress Level", 0, 10, 4)
    daily_steps = st.number_input("🚶 Daily Steps", 0, 50000, 6000)

with col3:
    heart_rate = st.number_input("💓 Heart Rate", 30, 200, 70)
    systolic = st.number_input("🩸 Systolic BP", 80, 200, 120)
    diastolic = st.number_input("🩸 Diastolic BP", 40, 150, 80)

st.markdown("---")

# Prediction button
if st.button("🔮 Predict Sleep Quality", use_container_width=True):
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

    try:
        response = requests.post("http://localhost:9696/predict", json=data)
        if response.status_code == 200:
            result = response.json()
            st.success(f"🌙 **Predicted Sleep Quality:** {result['sleep_quality']}")
            st.metric("Predicted Sleep Score", f"{result['sleep_prediction']:.2f}")
        else:
            st.error("⚠️ Prediction failed! Please check the backend service.")
    except Exception as e:
        st.error(f"❌ Error connecting to prediction service: {e}")

st.markdown("---")
st.caption("💡 Tip: Try adjusting your stress level or activity level to see how it impacts sleep quality!")
