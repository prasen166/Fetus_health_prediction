from flask import Flask, request, jsonify, render_template
import numpy as np
import pickle

app = Flask(__name__)

# Load the model
model = pickle.load(open('fetus_health_88.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()  # Get JSON data from POST request
        # Extract features from JSON data
        features = [
            float(data['baseline']), float(data['accelerations']), float(data['fetal_movement']),
            float(data['uterine_contractions']), float(data['light_decelerations']), float(data['severe_decelerations']),
            float(data['prolongued_decelerations']), float(data['abnormal_short_term_variability']),
            float(data['mean_value_of_short_term_variability']), float(data['percentage_of_time_with_abnormal_long_term_variability']),
            float(data['mean_value_of_long_term_variability']), float(data['histogram_width']), float(data['histogram_min']),
            float(data['histogram_max']), float(data['histogram_number_of_peaks']), float(data['histogram_number_of_zeroes']),
            float(data['histogram_mode']), float(data['histogram_mean']), float(data['histogram_median']), float(data['histogram_variance']),
            float(data['histogram_tendency'])
        ]
        # Convert features to numpy array and reshape for prediction
        features_arr = np.array(features).reshape(1, -1)

        # Make prediction using the model
        prediction = model.predict_proba(features_arr)

        # Determine the class label based on prediction
        result = ''
        if prediction[0, 0] > 0.5:
            result = 'Normal'
        elif prediction[0, 1] > 0.5:
            result = 'Suspect'
        elif prediction[0, 2] > 0.5:
            result = 'Pathological'
        else:
            result = 'Unknown'

        # Return prediction result as JSON
        return jsonify({'result': result})

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
