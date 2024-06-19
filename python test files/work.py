import pickle
from flask import Flask, request, jsonify

app = Flask(__name__)

# Load the pickled model
with open('fetus_health_88.pkl', 'rb') as model_file:
    model = pickle.load(model_file)


@app.route('/')
def home():
    return render_templates('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        # Collect input values
        baseline = float(request.form['baseline'])
        accelerations = float(request.form['accelerations'])
        fetal_movement = float(request.form['fetal_movement'])
        uterine_contractions = float(request.form['uterine_contractions'])
        light_decelerations = float(request.form['light_decelerations'])
        severe_decelerations = float(request.form['severe_decelerations'])
        prolongued_decelerations = float(request.form['prolongued_decelerations'])
        abnormal_short_term_variability = float(request.form['abnormal_short_term_variability'])
        mean_value_of_short_term_variability = float(request.form['mean_value_of_short_term_variability'])
        percentage_of_time_with_abnormal_long_term_variability = float(request.form['percentage_of_time_with_abnormal_long_term_variability'])
        mean_value_of_long_term_variability = float(request.form['mean_value_of_long_term_variability'])
        histogram_width = float(request.form['histogram_width'])
        histogram_min = float(request.form['histogram_min'])
        histogram_max = float(request.form['histogram_max'])
        histogram_number_of_peaks = float(request.form['histogram_number_of_peaks'])
        histogram_number_of_zeroes = float(request.form['histogram_number_of_zeroes'])
        histogram_mode = float(request.form['histogram_mode'])
        histogram_mean = float(request.form['histogram_mean'])
        histogram_median = float(request.form['histogram_median'])
        histogram_variance = float(request.form['histogram_variance'])
        histogram_tendency = float(request.form['histogram_tendency'])

        # Make prediction
        features = np.array([baseline, accelerations, fetal_movement, uterine_contractions, light_decelerations,
                             severe_decelerations, prolongued_decelerations, abnormal_short_term_variability,
                             mean_value_of_short_term_variability, percentage_of_time_with_abnormal_long_term_variability,
                             mean_value_of_long_term_variability, histogram_width, histogram_min, histogram_max,
                             histogram_number_of_peaks, histogram_number_of_zeroes, histogram_mode, histogram_mean,
                             histogram_median, histogram_variance, histogram_tendency]).reshape(1, -1)

        prediction = model.predict(features)[0]

        # Redirect based on prediction result
        if prediction == 1:
            return redirect(url_for('normal'))
        elif prediction == 2:
            return redirect(url_for('suspect'))
        elif prediction == 3:
            return redirect(url_for('pathological'))

@app.route('/normal')
def normal():
    return render_template('normal.html')

@app.route('/suspect')
def suspect():
    return render_template('suspect.html')

@app.route('/pathological')
def pathological():
    return render_template('pathological.html')

if __name__ == '__main__':
    app.run(debug=True)

