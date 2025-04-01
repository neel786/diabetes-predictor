# diabetes-predictor
A web app to predict diabetes using ML
# Diabetes Prediction Web Application

A machine learning-powered web app to predict diabetes using a Random Forest classifier, built with Flask.

## Features
- Predicts diabetes based on 8 health metrics (e.g., Glucose, BMI, Age).
- Modern, responsive UI with custom CSS styling.
- Real-time predictions via a web interface.

## Tech Stack
- Python, Flask, scikit-learn, Pandas, NumPy
- HTML, CSS (external stylesheet)

## How to Run
1. Clone the repo: `git clone https://github.com/neel786/diabetes-predictor.git`
2. Install dependencies: `pip install -r requirements.txt`
3. Train the model: `python train_model.py`
4. Run the app: `python app.py`
5. Open `http://127.0.0.1:5000/` in your browser.

## Dataset
- Uses the Pima Indians Diabetes Dataset (`diabetes.csv`).