from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Home route
@app.route('/')
def home():
    return render_template('index.html')

# Prediction route
@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        data = request.get_json()
        
        # Extract values from the JSON data
        baseline = data.get('baseline', 0.0)
        
        # Define thresholds for classification
        if 100 <= baseline < 120:
            predicted_category = 'Normal'
        elif 120 <= baseline < 140:
            predicted_category = 'Suspect'
        elif 140 <= baseline <= 160:
            predicted_category = 'Pathological'
        else:
            predicted_category = 'Unknown'  # Handle values outside defined ranges
        
        # Return the prediction result as JSON
        return jsonify({'predicted_category': predicted_category})

if __name__ == '__main__':
    app.run(debug=True)
