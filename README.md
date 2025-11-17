# Sleep Health Predictor

<p align="center">
  <img src="https://github.com/eadka/sleep-health-predictor/blob/main/images/sleep_health_predictor_logo.png" alt="SleepHealth" width="800" height="200"/>
</p>

A machine learning project analyzing how **lifestyle habits** like stress, BMI, and exercise influence **sleep quality**. 


## Project Overview
This project uses the [Sleep Health and Lifestyle Dataset](https://www.kaggle.com/datasets/uom190346a/sleep-health-and-lifestyle-dataset) to:
- Explore relationships between lifestyle factors and sleep quality.
- Predict **sleep quality** using ML models.
- Build an interpretable, deployable prediction pipeline.


## Dataset
The [*dataset*](https://www.kaggle.com/datasets/uom190346a/sleep-health-and-lifestyle-dataset) is imported into the [data](https://github.com/eadka/sleep-health-predictor/tree/main/data) folder and saved as *sleep_health_lifestyle.csv*.

*The data can also be downloaded by running the [kaggle-data-import](data/kaggle-data-import.ipynb) notebook.*

**Features include:**
- `Age`, `Gender`, `Occupation`, `Blood Pressure`, `Stress Level`, `Heart Rate`, `Physical Activity Level`, `Daily Steps`, `BMI`, `Sleep Duration`, `Sleep Disorder`
- Target: `Quality of Sleep` 


## Workflow
Data analysis and models training are conducted in the [sleep-health-predictor-notebook.ipynb](https://github.com/eadka/sleep-health-predictor/blob/main/notebooks/sleep-health-predictor-notebook.ipynb) Jupyter Notebook. 

Following steps are performed:

1. **Data Cleaning & Exploration**
2. **Feature Engineering**
3. **Exploratory Data Analysis**
4. **Model Training** – Linear Regression, Ridge Regression, Lasso, Decision Trees, Random Forest and XGBoost
5. **Model Evaluation** – **Grid Search** along with **Cross Validation** are used to tune the hyperparameters tuning. **R²**, **RMSE** and **MAE** are used to assess the results.
6. **Deployment** – Flask + Streamlit + Docker container

### 💤 Findings from Exploratory Data Analysis with *Quality of Sleep*

The below table shows the impact of correlation between individual features and Quality of Sleep.
<table style="table-layout: fixed; width: 100%; border-collapse: collapse;">
<tr><th>Type</th><th>Feature</th><th>Correlation</th><th>Interpretation</th></tr>

<tr>
<td><nobr>&uarr; <b>Pos</b></nobr></td>
<td><b>Age (29–59 yrs)</b></td>
<td><span style="color:MediumSeaGreen;"><b>Mild</b></span></td>
<td>Middle-aged individuals tend to report slightly better sleep quality.</td>
</tr>

<tr>
<td><nobr>&uarr; <b>Pos</b></nobr></td>
<td><b>Sleep Duration</b></td>
<td><span style="color:MediumSeaGreen;"><b>Strong</b></span></td>
<td>Longer sleep duration is associated with better sleep quality.</td>
</tr>

<tr>
<td><nobr>&uarr; <b>Pos</b></nobr></td>
<td><b>Physical Activity Level</b></td>
<td><span style="color:MediumSeaGreen;"><b>Weak</b></span></td>
<td>Regular exercise contributes to improved sleep quality.</td>
</tr>

<tr>
<td><nobr>&uarr; <b>Pos</b></nobr></td>
<td><b>Daily Steps</b></td>
<td><span style="color:MediumSeaGreen;"><b>Very Low</b></span></td>
<td>General movement has limited direct effect on sleep quality.</td>
</tr>

<tr>
<td><nobr>&darr; <b>Neg</b></nobr></td>
<td><b>Systolic BP</b></td>
<td><span style="color:Tomato;"><b>Weak</b></span></td>
<td>Higher systolic blood pressure is linked to poorer sleep quality.</td>
</tr>

<tr>
<td><nobr>&darr; <b>Neg</b></nobr></td>
<td><b>Diastolic BP</b></td>
<td><span style="color:Tomato;"><b>Weak</b></span></td>
<td>Higher diastolic pressure also correlates with lower sleep quality.</td>
</tr>

<tr>
<td><nobr>&darr; <b>Neg</b></nobr></td>
<td><b>Heart Rate</b></td>
<td><span style="color:Tomato;"><b>Weak</b></span></td>
<td>Higher heart rates are associated with reduced sleep quality.</td>
</tr>

<tr>
<td><nobr>&darr; <b>Neg</b></nobr></td>
<td><b>Stress Level</b></td>
<td><span style="color:Tomato;"><b>Strong</b></span></td>
<td>Increased stress leads to significantly poorer sleep quality.</td>
</tr>
</table>

---

### ⭐️ Results of Model Training and Evaluation

Models trained and evaluated are: Linear Regression, Ridge Regression, Lasso, Decision Trees, Random Forest and XGBoost

**Grid Search** along with **Cross Validation** are used to tune the hyperparameters to ensure we enable better parameter interactions and get more robust results. 

**R²**, **RMSE** (Root Mean Squared Error) and **MAE** (Mean Absolute Error) are used to evaluate the results.


The below table shows the results of the **Baseline** and **Tuned** models. 


| Model                 | R² (Baseline) | RMSE (Baseline) | MAE (Baseline) | R² (Tuned) | RMSE (Tuned) | MAE (Tuned) |
| --------------------- | ------------- | --------------- | -------------- | ---------- | ------------ | ----------- |
| **Linear Regression** | 0.966         | 0.255           | 0.153          | 0.963      | 0.264        | 0.161       |
| **Ridge Regression**  | 0.964         | 0.261           | 0.166          | 0.957      | 0.286        | 0.193       |
| **Lasso**             | 0.044         | 1.348           | 1.189          | 0.954      | 0.295        | 0.205       |
| **Decision Tree**     | 0.986         | 0.163           | 0.027          | 0.967      | 0.250        | 0.077       |
| **Random Forest**     | 0.979         | 0.200           | 0.059          | 0.983      | 0.178        | 0.050       |
|🥇**XGBoost**         | 0.980         | 0.194           | 0.031          | 0.985      | 0.171        | 0.055       |


### 🏆 Winning Model

**XGBoost** achieved the **highest R²** (0.985) and **lowest RMSE** (0.171) among all tuned models, indicating it’s the **most robust** model for predicting `quality_of_sleep`.


## Steps to run the application
### 1. Docker Build 

Build the Docker image

```
docker build -t sleep-predictor .
```


### 2. Run Container

```
docker run -p 9696:9696 sleep-predictor
```

You should see logs like:

```
[2025-11-06 07:45:22 +0000] [1] [INFO] Starting gunicorn 21.2.0
[2025-11-06 07:45:22 +0000] [1] [INFO] Listening at: http://0.0.0.0:9696 (1)
...
```

### 3. Test Endpoint:
In another terminal, test the app with an example sleep data:
```
curl -X POST -H "Content-Type: application/json" \
  -d '{
    "gender": "Female",
    "age": 57,
    "occupation": "Nurse",
    "sleep_duration": 8.2,
    "physical_activity_level": 75,
    "stress_level": 3,
    "bmi_category": "Overweight",
    "heart_rate": 68,
    "daily_steps": 7000,
    "systolic": 140,
    "diastolic": 95,
    "sleep_disorder": "Sleep Apnea"
  }' \
  http://localhost:9696/predict
```

### 4. Result
You should get back JSON like:

```
{
  "sleep_prediction": 7.4,
  "sleep_quality": "Good"
}
```

### 5. Docker Close
To clean up all the containers, images, networks and caches:

```
docker system prune -a --volumes
```

## 🎈 StreamLit
Alternatively you can run the stream lit app for a visual alteration of the input parameters and to get a prediction on sleep quality.


To run the **StreamLit** app, open a terminal and run the below command:
```
 pipenv shell
 cd notebooks/
 streamlit run app.py
 ```

Open the StreamLit app in a browser or go to **Ports** and open **8501** or the port mapped for the StreamLit app. 

<p align="center">
  <img src="https://github.com/eadka/sleep-health-predictor/blob/main/images/StreamLitApp_sleep_health_predictor.png" alt="StreamLit App" width="800"/>
</p>

Add in the data and click on **Predict Sleep Quality** button to see the sleep quality prediction.

<p align="center">
  <img src="https://github.com/eadka/sleep-health-predictor/blob/main/images/StreamLitAppResult_sleep_health_predictor.png" alt="StreamLit App" width="600"/>
</p>


## ☁️ Cloud deployment with **fly.io**
The Flask service is fully Dockerized and deployed to Fly.io, providing a secure and scalable cloud endpoint for predictions.

The animation below shows the app *muddy-wind-5020* running in fly.io. This is passed as the URL in [**predict-test.py**](notebooks/predict_test.py) which when run uses the model deployed in the cloud to evaluate and return the result. 

![Demo](images/flyio_deployment.gif)


## 😴 Overall Insights on Sleep Quality

Overall, <b>sleep duration</b> and <b>stress level</b> emerge as the most influential factors affecting sleep quality.  
While longer sleep and regular physical activity tend to enhance rest quality, elevated <b>stress</b>, <b>heart rate</b>, and <b>blood pressure</b> correspond with poorer sleep outcomes.  

💡 Maintaining a <b>balanced lifestyle</b> — combining adequate rest, consistent exercise, and stress management — can meaningfully improve overall sleep quality.

