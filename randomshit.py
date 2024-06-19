from flask import Flask, render_template, request, jsonify
import joblib
import pickle


app = Flask(__name__)

# Load the pickled model
with open('fetus_health_88.pkl', 'rb') as model_file:
    model = pickle.load(model_file)


# Load your machine learning model
# Example:
# model = joblib.load('path_to_your_model.pkl')

# Define a function to make predictions
def make_prediction(input_data):
    # Example function, replace with your model prediction logic
    def make_prediction(input_data):
    # Assuming model.predict() returns a single prediction, not an array
     prediction = model.predict(input_data)[0]  # Assuming it's a single prediction
     return {'predicted_category': prediction}

# Route to render the HTML page
@app.route('/')
def form():
    return render_template('index.html')

# Route to handle prediction request
@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()

    # Extract data from JSON request
    baseline = data['baseline']
    accelerations = data['accelerations']
    fetal_movement = data['fetal_movement']
    uterine_contractions = data['uterine_contractions']
    light_decelerations = data['light_decelerations']
    severe_decelerations = data['severe_decelerations']
    prolongued_decelerations = data['prolongued_decelerations']
    abnormal_short_term_variability = data['abnormal_short_term_variability']
    mean_value_of_short_term_variability = data['mean_value_of_short_term_variability']
    percentage_of_time_with_abnormal_long_term_variability = data['percentage_of_time_with_abnormal_long_term_variability']
    mean_value_of_long_term_variability = data['mean_value_of_long_term_variability']
    histogram_width = data['histogram_width']
    histogram_min = data['histogram_min']
    histogram_max = data['histogram_max']
    histogram_number_of_peaks = data['histogram_number_of_peaks']
    histogram_number_of_zeroes = data['histogram_number_of_zeroes']
    histogram_mode = data['histogram_mode']
    histogram_mean = data['histogram_mean']
    histogram_median = data['histogram_median']
    histogram_variance = data['histogram_variance']
    histogram_tendency = data['histogram_tendency']

    # Make prediction
    input_data = [[baseline, accelerations, fetal_movement, uterine_contractions, light_decelerations,
                   severe_decelerations, prolongued_decelerations, abnormal_short_term_variability,
                   mean_value_of_short_term_variability, percentage_of_time_with_abnormal_long_term_variability,
                   mean_value_of_long_term_variability, histogram_width, histogram_min, histogram_max,
                   histogram_number_of_peaks, histogram_number_of_zeroes, histogram_mode, histogram_mean,
                   histogram_median, histogram_variance, histogram_tendency]]

    prediction_result = make_prediction(input_data)

    # Return prediction result as JSON
    return jsonify(prediction_result)

if __name__ == '__main__':
    app.run(debug=True)
