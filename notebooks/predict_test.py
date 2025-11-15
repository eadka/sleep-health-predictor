import requests

url = "http://127.0.0.1:9696/predict"

sample_individual = {
    "gender": "Female",
    "age": 57,
    "occupation": "Nurse",
    "sleep_duration": 8.2,
    "physical_activity_level": 75,
    "stress_level": 3,
    "bmi_category": "Overweight",
    "heart_rate": 68,
    "daily_steps": 7000,
    "sleep_disorder": "Sleep Apnea",
    "systolic": 140,
    "diastolic": 95
}

sample_poor_sleep = {
    "gender": "Male",
    "age": 32,
    "occupation": "Sales Representative",
    "sleep_duration": 4.5,
    "physical_activity_level": 20,
    "stress_level": 8,
    "bmi_category": "Obese",
    "heart_rate": 90,
    "daily_steps": 2500,
    "sleep_disorder": "Insomnia",
    "systolic": 150,
    "diastolic": 100
}

sample_avg_sleep = {
    "gender": "Female",
    "age": 45,
    "occupation": "Teacher",
    "sleep_duration": 6.8,
    "physical_activity_level": 50,
    "stress_level": 5,
    "bmi_category": "Overweight",
    "heart_rate": 78,
    "daily_steps": 5000,
    "sleep_disorder": "None",
    "systolic": 130,
    "diastolic": 85
}

sample_good_sleep = {
    "gender": "Female",
    "age": 28,
    "occupation": "Engineer",
    "sleep_duration": 8.5,
    "physical_activity_level": 80,
    "stress_level": 2,
    "bmi_category": "Normal",
    "heart_rate": 65,
    "daily_steps": 9500,
    "sleep_disorder": "None",
    "systolic": 115,
    "diastolic": 75
}

# send POST request
# requests.post(url, json=sample_individual)
response = requests.post(url, json=sample_poor_sleep)

# print response details for debugging
print("Response Status code:", response.status_code)
print("Response Text:", response.text)
print()

# try parsing JSON if valid
try:
    result = response.json()
    print("Parsed JSON:", result)
    print("Predicted Sleep Quality:", result.get("sleep_quality"))
except Exception as e:
    print("Error decoding JSON:", e)
    print("Raw response:", response.text)