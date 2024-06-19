from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

def classify_category(input_data):
    # Basic classification logic based on input data
    # You can define your own rules here based on the input data attributes
    
    if input_data['abnormal_short_term_variability'] > 20 or input_data['percentage_of_time_with_abnormal_long_term_variability'] > 60:
        return 'Pathological'
    elif input_data['baseline value'] > 140 or input_data['mean_value_of_long_term_variability'] > 60:
        return 'Suspect'
    else:
        return 'Normal'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    input_data = request.json
    
    # Classify the category based on input data
    predicted_category = classify_category(input_data)
    
    return jsonify({'predicted_category': predicted_category})

if __name__ == '__main__':
    app.run(debug=True)
