from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    # Perform prediction logic here
    # For demonstration, let's assume we have a function predict_category() that returns the predicted category
    predicted_category = predict_category(data)
    
    result = {'predicted_category': predicted_category}
    return jsonify(result)

def predict_category(data):
    # Here you can implement your actual prediction logic based on the input data
    # For demonstration, let's just assume some dummy logic
    # You would replace this with your machine learning model or any other logic
    
    # Example dummy logic:
    baseline = data.get('baseline', 0)
    if baseline > 130:
        return 'Pathological'
    elif baseline > 120:
        return 'Suspect'
    else:
        return 'Normal'

if __name__ == '__main__':
    app.run(debug=True)
