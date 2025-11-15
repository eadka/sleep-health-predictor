import pickle
import pandas as pd
from flask import Flask 
from flask import request
from flask import jsonify

# ### Loading the model
input_file = 'model_pipeline.bin'


with open(input_file, 'rb') as f_in:
    pipe_ret = pickle.load(f_in)


app = Flask('sleep-health')

@app.route('/predict', methods=['POST'])
def predict():
    sample_individual = request.get_json()


    df_sample = pd.DataFrame([sample_individual])

    # Added for debugging:
    expected = getattr(pipe_ret, "feature_names_in_", None)
    print("Expected columns:", expected)
    print("Input columns:", df_sample.columns.tolist())


    y_pred = pipe_ret.predict(df_sample)
    # Map to categories
    if y_pred[0] <= 5:
        quality = "Poor"
    elif y_pred[0]  <= 7:
        quality = "Average"
    else:
        quality = "Good"

    result = {
        "sleep_prediction": float(y_pred[0]),
        "sleep_quality": quality
    }
    return jsonify(result)



if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=9696)