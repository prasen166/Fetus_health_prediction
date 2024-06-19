from flask import Flask, render_template, request, jsonify
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier

app = Flask(__name__)

# Load the dataset
data = pd.read_csv('fetal_health.csv')

# Features and target
X = data.drop('fetal_health', axis=1)
y = data['fetal_health']

# Standardize the features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Initialize the kNN classifier
knn = KNeighborsClassifier(n_neighbors=5, weights='distance')

# Train the classifier
knn.fit(X_scaled, y)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Get data from request
    data = request.get_json()

    # Convert data to numpy array
    input_data = np.array(list(data.values())).reshape(1, -1)

    # Scale input data
    input_scaled = scaler.transform(input_data)

    # Make prediction
    prediction = knn.predict(input_scaled)[0]

    # Map prediction to category
    category_mapping = {1: 'Normal', 2: 'Suspect', 3: 'Pathological'}
    predicted_category = category_mapping[prediction]

    # Redirect to the appropriate page based on predicted category
    if predicted_category == 'Normal':
        return render_template('normal.html')
    elif predicted_category == 'Suspect':
        return render_template('suspect.html')
    elif predicted_category == 'Pathological':
        return render_template('pathological.html')

if __name__ == '__main__':
    app.run(debug=True)
