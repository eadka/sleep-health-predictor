# app.py
import os
import streamlit as st
import streamlit.components.v1 as components
import requests

# PORT = int(os.environ.get("PORT", 8501))  # Fly.io sets this automatically
# API_URL = os.environ.get("API_URL", "http://localhost:9696/predict") 

# ---- Page Setup ----
st.set_page_config(page_title="🌙 Sleep Quality Predictor", layout="wide")

# ---- Header Section ----
col_logo, col_title = st.columns([1, 5])
with col_logo:
    st.image(
        "https://cdn-icons-png.flaticon.com/512/4151/4151022.png",  # moon/bed icon
        width=80,
    )
with col_title:
    st.title("🌙 Sleep Quality Predictor")
    st.markdown("#### Discover how your lifestyle habits influence your sleep! 💤")

st.markdown("---")

# ---- Input Layout ----
col1, col2, col3 = st.columns(3)

with col1:
    gender = st.selectbox("👩‍🦰 Gender", ["Male", "Female"])
    age = st.number_input("🎂 Age", min_value=18, max_value=100, value=30)
    occupation = st.text_input("💼 Occupation", "Engineer")
    bmi_category = st.selectbox("⚖️ BMI Category", ["Normal", "Overweight", "Obese"])
    sleep_disorder = st.selectbox("🧠 Sleep Disorder", ["None", "Insomnia", "Sleep Apnea"])

with col2:
    sleep_duration = st.number_input("🕒 Sleep Duration (hrs)", min_value=0.0, max_value=12.0, value=7.5)
    physical_activity_level = st.slider("🏃 Physical Activity Level (Mins Exercised)", 0, 100, 50)
    stress_level = st.slider("😫 Stress Level", 0, 10, 4)
    daily_steps = st.number_input("🚶 Daily Steps", 0, 50000, 6000)

with col3:
    heart_rate = st.number_input("💓 Heart Rate", 30, 200, 70)
    systolic = st.number_input("🩸 Systolic BP", 80, 200, 120)
    diastolic = st.number_input("💉 Diastolic BP", 40, 150, 80)

# ---- Predict Button ----
st.markdown("---")
center_button = st.columns([4, 2, 4])[1]
with center_button:
    predict_clicked = st.button("🔮 Predict Sleep Quality", use_container_width=True)

# ---- Prediction Logic ----
if predict_clicked:
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
        "diastolic": diastolic,
    }

    try:
        # API_URL = "https://falling-butterfly-5988.fly.dev/predict"
        response = requests.post("http://localhost:9696/predict", json=data)
        # response = requests.post(API_URL, json=data)
        if response.status_code == 200:
            result = response.json()
            sleep_quality = result['sleep_quality']

            # ---- Color mapping ----
            color_map = {
                "Poor": "#E74C3C",      # red
                "Average": "#F1C40F",   # yellow
                "Good": "#27AE60"       # green
            }
            color = color_map.get(sleep_quality, "#2E86C1")  # default blue

            # ---- Dramatic Result Display with Emojis ----
            emoji_map = {
                "Poor": "⚠️",      # warning
                "Average": "😴",   # sleeping face
                "Good": "🛌"       # bed
            }
            emoji = emoji_map.get(sleep_quality, "💤")

            st.markdown("## 💤 Prediction Result")
            col_a, col_b, col_c = st.columns([1, 2, 1])
            with col_b:
                components.html(
                    f"""
                    <div style="text-align:center; background-color:#f5f5f5;
                                padding:20px; border-radius:20px;
                                box-shadow: 0px 4px 15px rgba(0,0,0,0.2);">

                        <h1 style="color:{color}; font-size:50px; margin-bottom:5px;">
                            {emoji} {sleep_quality}
                        </h1>

                        <div style="font-size:28px; margin-top:5px;">
                            <strong>Predicted Sleep Score:</strong>
                            <span style="font-weight:800;">{result['sleep_prediction']:.2f}</span>
                        </div>

                    </div>
                    """,
                    height=300
                )


        else:
            st.error("⚠️ Prediction failed! Please check your backend service.")
    except Exception as e:
        st.error(f"❌ Error connecting to the prediction API: {e}")

# ---- Footer ----
st.markdown("---")
st.caption("💡 Tip: Adjust your stress or activity levels to explore how they affect your sleep quality.")
