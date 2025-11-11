# Sleep Health Predictor
A machine learning project analyzing how **lifestyle habits** like stress, BMI, and screen time influence **sleep quality and disorders**.


## Project Overview
This project uses the [Sleep Health and Lifestyle Dataset](https://www.kaggle.com/datasets/uom190346a/sleep-health-and-lifestyle-dataset) to:
- Explore relationships between lifestyle factors and sleep quality.
- Predict the presence of a **sleep disorder** using ML models.
- Build an interpretable, deployable prediction pipeline.


## Dataset
**Source:** Kaggle — [*Sleep Health and Lifestyle Dataset*](https://www.kaggle.com/datasets/uom190346a/sleep-health-and-lifestyle-dataset) 

The dataset is imported from the above source into the [data](https://github.com/eadka/sleep-health-predictor/tree/main/data) folder
and saved as sleep_health_lifestyle.csv.

**Features include:**
- `Sleep Duration`, `Stress Level`, `Physical Activity Level`, `BMI`, `Screen Time`, <<<fill here>>>
- Target: `Sleep Disorder` (binary classification)

## Workflow
1. **Data Cleaning & Exploration**


2. **Feature Engineering**

3. **Exploratory Data Analysis**
## 💤 Findings from Correlation Analysis with *Quality of Sleep*

<table>
<tr><th>Type</th><th>Feature</th><th>Correlation</th><th>Interpretation</th></tr>

<tr>
<td>🔹 <b>Positive</b></td>
<td><b>Age (29–59 yrs)</b></td>
<td><span style="color:MediumSeaGreen;"><b>Mild</b></span></td>
<td>Middle-aged individuals tend to report slightly better sleep quality.</td>
</tr>

<tr>
<td>🔹 <b>Positive</b></td>
<td><b>Sleep Duration</b></td>
<td><span style="color:MediumSeaGreen;"><b>Strong</b></span></td>
<td>Longer sleep duration is associated with better sleep quality.</td>
</tr>

<tr>
<td>🔹 <b>Positive</b></td>
<td><b>Physical Activity Level</b></td>
<td><span style="color:MediumSeaGreen;"><b>Weak</b></span></td>
<td>Regular exercise contributes to improved sleep quality.</td>
</tr>

<tr>
<td>🔹 <b>Positive</b></td>
<td><b>Daily Steps</b></td>
<td><span style="color:MediumSeaGreen;"><b>Very Low</b></span></td>
<td>General movement has limited direct effect on sleep quality.</td>
</tr>

<tr>
<td>🔻 <b>Negative</b></td>
<td><b>Systolic BP</b></td>
<td><span style="color:Tomato;"><b>Weak</b></span></td>
<td>Higher systolic blood pressure is linked to poorer sleep quality.</td>
</tr>

<tr>
<td>🔻 <b>Negative</b></td>
<td><b>Diastolic BP</b></td>
<td><span style="color:Tomato;"><b>Weak</b></span></td>
<td>Higher diastolic pressure also correlates with lower sleep quality.</td>
</tr>

<tr>
<td>🔻 <b>Negative</b></td>
<td><b>Heart Rate</b></td>
<td><span style="color:Tomato;"><b>Weak</b></span></td>
<td>Higher heart rates are associated with reduced sleep quality.</td>
</tr>

<tr>
<td>🔻 <b>Negative</b></td>
<td><b>Stress Level</b></td>
<td><span style="color:Tomato;"><b>Strong</b></span></td>
<td>Increased stress leads to significantly poorer sleep quality.</td>
</tr>
</table>

---

### 🧠 Insights Summary

Overall, <b>sleep duration</b> and <b>stress level</b> emerge as the most influential factors affecting sleep quality.  
While longer sleep and regular physical activity tend to enhance rest quality, elevated <b>stress</b>, <b>heart rate</b>, and <b>blood pressure</b> correspond with poorer sleep outcomes.  

💡 Maintaining a <b>balanced lifestyle</b> — combining adequate rest, consistent exercise, and stress management — can meaningfully improve overall sleep quality.



3. **Model Training** – Random Forest, XGBoost, etc.


4. **Model Evaluation** – ROC AUC, feature importance


5. **Deployment** – FastAPI app + Docker container

