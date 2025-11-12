import pickle
import pandas as pd
from flask import Flask, request, jsonify

# Initialize Flask app
app = Flask('sleep_health')

# Load the model pipeline
input_file = 'model_pipeline.bin'
with open(input_file, 'rb') as f_in:
    pipe_ret = pickle.load(f_in)

@app.route('/predict', methods=['POST'])
def predict():
    individual = request.get_json()

    # Convert to DataFrame (single row)
    df_individual = pd.DataFrame([individual])

    # Make prediction
    y_pred = pipe_ret.predict(df_individual)
    y_pred_value = float(y_pred[0])  

    # Categorize sleep quality
    if y_pred_value <= 5:
        quality = 'Poor'
    elif 5 < y_pred_value <= 7:
        quality = 'Average'
    else:
        quality = 'Good'

    # Build response
    result = {
        'sleep_prediction': y_pred_value,
        'sleep_quality': quality
    }

    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=9696)
