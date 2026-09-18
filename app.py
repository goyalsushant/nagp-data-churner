from flask import Flask, request, jsonify
import pandas as pd
import numpy as np
import joblib
from feature_engineering import ChurnFeatureEngineer


app = Flask(__name__)


# Load the complete trained pipeline
model = joblib.load("model/churn_model.pkl")


# Expected input columns
REQUIRED_COLUMNS = [
    "gender",
    "SeniorCitizen",
    "Partner",
    "Dependents",
    "tenure",
    "PhoneService",
    "MultipleLines",
    "InternetService",
    "OnlineSecurity",
    "OnlineBackup",
    "DeviceProtection",
    "TechSupport",
    "StreamingTV",
    "StreamingMovies",
    "Contract",
    "PaperlessBilling",
    "PaymentMethod",
    "MonthlyCharges",
    "TotalCharges"
]


@app.route("/", methods=["GET"])
def home():
    return jsonify({
        "message": "Customer Churn Prediction API",
        "endpoint": "POST /predict"
    })


@app.route("/predict", methods=["POST"])
def predict():

    try:

        # Get JSON request
        data = request.get_json()

        if data is None:
            return jsonify({
                "error": "Request body must contain valid JSON."
            }), 400

        # Check required fields
        missing_fields = [
            column
            for column in REQUIRED_COLUMNS
            if column not in data
        ]

        if missing_fields:
            return jsonify({
                "error": "Missing required fields.",
                "missing_fields": missing_fields
            }), 400

        # Create DataFrame
        input_data = pd.DataFrame(
            [data]
        )

        # Ensure correct column order
        input_data = input_data[
            REQUIRED_COLUMNS
        ]

        # Convert numeric fields
        numeric_columns = [
            "SeniorCitizen",
            "tenure",
            "MonthlyCharges",
            "TotalCharges"
        ]

        for column in numeric_columns:
            input_data[column] = pd.to_numeric(
                input_data[column],
                errors="coerce"
            )

        # Check numeric values
        if input_data[numeric_columns].isnull().any().any():

            invalid_columns = (
                input_data[numeric_columns]
                .columns[
                    input_data[numeric_columns]
                    .isnull()
                    .any()
                ]
                .tolist()
            )

            return jsonify({
                "error": "Invalid numeric value.",
                "invalid_fields": invalid_columns
            }), 400

        # Make prediction
        prediction = model.predict(
            input_data
        )[0]

        probability = model.predict_proba(
            input_data
        )[0][1]

        # Convert prediction to Yes / No
        churn_prediction = (
            "Yes"
            if prediction == 1
            else "No"
        )

        return jsonify({
            "prediction": churn_prediction,
            "churn_probability": round(
                float(probability),
                4
            )
        })

    except Exception as e:

        return jsonify({
            "error": "Unable to process prediction.",
            "details": str(e)
        }), 500


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )
