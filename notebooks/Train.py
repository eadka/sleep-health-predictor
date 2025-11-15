#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import pickle


# In[2]:


from sklearn.model_selection import train_test_split
from sklearn.metrics import root_mean_squared_error, mean_absolute_error
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.impute import SimpleImputer
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from xgboost import XGBRegressor


# In[3]:


# Read data
df = pd.read_csv('../data/sleep_health_lifestyle.csv')
df.columns = df.columns.str.lower().str.replace(' ', '_')

# Separate the numeric and categorical columns
numerical = df.columns[(df.dtypes == 'int64') | (df.dtypes == 'float64')]
categorical = df.columns[(df.dtypes == 'object')]

# Feature engineering and data preparation
df['sleep_disorder'] = df['sleep_disorder'].fillna('None')
bp_split = df['blood_pressure'].str.split('/', expand=True)
df['systolic'] = bp_split[0].astype(int)
df['diastolic'] = bp_split[1].astype(int)
df.loc[df['bmi_category'] == 'Normal Weight', 'bmi_category'] = 'Normal'


del df['blood_pressure']
del df['person_id']

numerical = numerical.difference(['quality_of_sleep', 'person_id'])
categorical = categorical.difference(['blood_pressure'])


# In[4]:


# Split the data into train, validation and test sets
df_full_train, df_test = train_test_split(df, test_size=0.2, random_state=1)
df_train, df_val = train_test_split(df_full_train, test_size=0.25, random_state=1)

df_full_train = df_full_train.reset_index(drop=True)
df_train = df_train.reset_index(drop=True)
df_val = df_val.reset_index(drop=True)
df_test = df_test.reset_index(drop=True)

y_full_train = df_full_train.quality_of_sleep
y_train = df_train.quality_of_sleep
y_val = df_val.quality_of_sleep
y_test = df_test.quality_of_sleep

del df_full_train['quality_of_sleep']
del df_train['quality_of_sleep']
del df_val['quality_of_sleep']
del df_test['quality_of_sleep']


# In[5]:


# Pipeline for categorical columns
categorical_transformer = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='constant',fill_value='None')),
    ('encoder', OneHotEncoder(handle_unknown='ignore'))
])

# Pipeline for numerical columns
numerical_transformer = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='median')),
    ('scaler', StandardScaler())
])


preprocessor = ColumnTransformer(transformers=[
    ('cat', categorical_transformer, categorical),
    ('num', numerical_transformer, numerical)
])


# In[6]:


def train(X_train, y_train, model_params, preprocessor):

    for name, (model, params) in model_params.items():
        pipe = Pipeline(steps=[
            ('preprocessor', preprocessor),
            ('model', model)
        ])

        ## Apply the tuned params
        pipe.set_params(**params)

        pipe.fit(X_train, y_train)

    return pipe


# In[7]:


model_params = {
    "XGBoost": (
        XGBRegressor(
            random_state=1,
            objective='reg:squarederror',
            enable_categorical=True,
            n_jobs=-1
        ),
        {
            'model__learning_rate': 0.2,
            'model__max_depth': 2,
            'model__n_estimators': 200,
            'model__subsample': 0.8,
            'model__colsample_bytree': 0.8,
            'model__reg_lambda': 10
        }
    )
}


# In[8]:


def predict(X_test, pipeline):

    # Calculate rmse and mae
    y_pred = pipeline.predict(X_test)

    return y_pred


# In[9]:


pipe_ret = train(df_full_train, y_full_train, model_params, preprocessor)
y_pred = predict(df_test, pipe_ret)
y_pred


# #### Saving the pipeline

# In[16]:


output_file = 'model_pipeline.bin'


# Lets write the pipeline of the model

# In[17]:


with open(output_file, 'wb') as f_out:
    pickle.dump(pipe_ret, f_out)

print(f"✅ Model pipeline saved successfully as {output_file}!")


# #### Loading the Pipeline

# In[22]:


input_file = 'model_pipeline.bin'


# In[23]:


with open(input_file, 'rb') as f_in:
    pipe_ret = pickle.load(f_in)


# In[24]:


pipe_ret


# In[12]:


# # Example dummy input for testing your model
# sample_individual = {
#     "gender": "Female",
#     "age": 45,
#     "occupation": "Engineer",
#     "sleep_duration": 7.5,
#     "physical_activity_level": 60,
#     "stress_level": 4,
#     "bmi_category": "Normal",
#     "heart_rate": 70,
#     "daily_steps": 8000,
#     "sleep_disorder": "None",
#     "systolic": 120,
#     "diastolic": 80
# }


# In[18]:


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


# In[19]:


df_sample = pd.DataFrame([sample_individual])
predicted_quality = pipe_ret.predict(df_sample)
print(f"Predicted Quality of Sleep: {predicted_quality[0]:.2f}")


# In[21]:


df_full_train.iloc[0]


# Actual value of the sleep 

# In[22]:


y_full_train.iloc[0]


# In[23]:


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

df_sample = pd.DataFrame([sample_poor_sleep])
predicted_quality = pipe_ret.predict(df_sample)
print(f"Predicted Quality of Sleep: {predicted_quality[0]:.2f}")


# In[25]:


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

df_sample = pd.DataFrame([sample_avg_sleep])
predicted_quality = pipe_ret.predict(df_sample)
print(f"Predicted Quality of Sleep: {predicted_quality[0]:.2f}")


# In[ ]:




