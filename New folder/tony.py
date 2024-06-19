from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Process form data
        baseline = float(request.form.get('baseline', 0))
        accelerations = float(request.form.get('accelerations', 0))
        fetal_movement = float(request.form.get('fetal_movement', 0))
        uterine_contractions = float(request.form.get('uterine_contractions', 0))
        light_decelerations = float(request.form.get('light_decelerations', 0))
        severe_decelerations = float(request.form.get('severe_decelerations', 0))
        prolongued_decelerations = float(request.form.get('prolongued_decelerations', 0))
        abnormal_short_term_variability = float(request.form.get('abnormal_short_term_variability', 0))
        mean_value_of_short_term_variability = float(request.form.get('mean_value_of_short_term_variability', 0))
        percentage_of_time_with_abnormal_long_term_variability = float(request.form.get('percentage_of_time_with_abnormal_long_term_variability', 0))
        mean_value_of_long_term_variability = float(request.form.get('mean_value_of_long_term_variability', 0))
        histogram_width = float(request.form.get('histogram_width', 0))
        histogram_min = float(request.form.get('histogram_min', 0))
        histogram_max = float(request.form.get('histogram_max', 0))
        histogram_number_of_peaks = float(request.form.get('histogram_number_of_peaks', 0))
        histogram_number_of_zeroes = float(request.form.get('histogram_number_of_zeroes', 0))
        histogram_mode = float(request.form.get('histogram_mode', 0))
        histogram_mean = float(request.form.get('histogram_mean', 0))
        histogram_median = float(request.form.get('histogram_median', 0))
        histogram_variance = float(request.form.get('histogram_variance', 0))
        histogram_tendency = float(request.form.get('histogram_tendency', 0))

        # Dummy prediction logic (replace this with your actual prediction logic)
        # Here, we're just using a simple if-elif-else based on the baseline value for demonstration
        if baseline < 5:
            prediction = "Normal"
        elif baseline < 10:
            prediction = "Suspect"
        else:
            prediction = "Pathological"

        # Redirect to appropriate page based on prediction
        if prediction == "Normal":
            return redirect(url_for('normal_page'))
        elif prediction == "Suspect":
            return redirect(url_for('suspect_page'))
        else:
            return redirect(url_for('pathological_page'))

    return render_template('index.html')

@app.route('/normal')
def normal_page():
    return render_template('normal.html')

@app.route('/suspect')
def suspect_page():
    return render_template('suspect.html')

@app.route('/pathological')
def pathological_page():
    return render_template('pathological.html')

if __name__ == '__main__':
    app.run(debug=True)
