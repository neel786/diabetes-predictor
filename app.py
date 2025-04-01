from flask import Flask, request, render_template
import joblib
import numpy as np

app = Flask(__name__)

# Load the trained model
model = joblib.load('diabetes_model.pkl')

@app.route('/', methods=['GET', 'POST'])
def home():
    prediction = None
    if request.method == 'POST':
        # Get form data
        pregnancies = float(request.form['pregnancies'])
        glucose = float(request.form['glucose'])
        bloodpressure = float(request.form['bloodpressure'])
        skinthickness = float(request.form['skinthickness'])
        insulin = float(request.form['insulin'])
        bmi = float(request.form['bmi'])
        dpf = float(request.form['dpf'])  # Diabetes Pedigree Function
        age = float(request.form['age'])

        # Prepare input for model
        input_data = np.array([[pregnancies, glucose, bloodpressure, skinthickness, 
                                insulin, bmi, dpf, age]])
        prediction = model.predict(input_data)[0]
        result = 'Diabetic' if prediction == 1 else 'Not Diabetic'
        return render_template('index.html', prediction=result)

    return render_template('index.html', prediction=prediction)

if __name__ == '__main__':
    app.run(debug=True)