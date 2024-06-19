from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    predicted_category = predict_category(data)
    
    if predicted_category == 'Normal':
        return jsonify({'redirect_url': '/normal'})
    elif predicted_category == 'Suspect':
        return jsonify({'redirect_url': '/suspect'})
    elif predicted_category == 'Pathological':
        return jsonify({'redirect_url': '/pathological'})

def predict_category(data):
    # Dummy logic for demonstration
    baseline = data.get('baseline', 0)
    if baseline > 130:
        return 'Pathological'
    elif baseline > 120:
        return 'Suspect'
    else:
        return 'Normal'

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

