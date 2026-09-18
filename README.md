### Customer Churn Prediction
# 1. Project Overview
This project develops an end-to-end machine learning solution for predicting customer churn for a telecommunications company.

The objective is to identify customers who are likely to churn so that the retention team can proactively consider appropriate retention actions.

The project uses the IBM Telco Customer Churn dataset and a Decision Tree Classifier.

* The complete workflow includes:
* Data understanding and preparation
* Exploratory Data Analysis
* Feature engineering
* Decision Tree model development
* Model comparison
* Model evaluation
* Model interpretation
* Model serialization
* REST API development using Flask

# 2. Business Problem
Customer churn can negatively affect the revenue and growth of a telecommunications company.

The objective of this project is to build a machine learning model that predicts whether an individual customer is likely to churn.

The target variable is:
```text
Churn
```

where:

* `Yes` = customer churned

* `No` = customer did not churn

The model can potentially support a retention team by identifying customers who may require further attention.

# 3. Dataset
The project uses the IBM Telco Customer Churn dataset.

The dataset contains customer demographic information, account information, and subscribed services.

Examples of variables include:

* Gender
* SeniorCitizen
* Partner
* Dependents
* Tenure
* PhoneService
* InternetService
* Contract
* PaymentMethod
* MonthlyCharges
* TotalCharges
* Churn

The dataset is stored in:
```text
data/Telco-Customer-Churn.csv
```

# 4. Machine Learning Workflow
The project follows this workflow:
```text
Raw Dataset
     |
     v
Data Understanding
     |
     v
Data Cleaning
     |
     v
Exploratory Data Analysis
     |
     v
Feature Engineering
     |
     v
Train/Test Split
     |
     v
Preprocessing
     |
     v
Decision Tree Models
     |
     v
Model Evaluation
     |
     v
Model Interpretation
     |
     v
Complete ML Pipeline
     |
     v
Flask REST API
```
# 5. Data Preparation
The dataset was inspected for:

* Data types
* Missing values
* Duplicate records
* Numerical variables
* Categorical variables
* Target distribution

Categorical variables were converted into numerical representations using one-hot encoding.

Numerical variables were handled using appropriate numerical preprocessing.

The train/test split uses:
```text
Training data: 70%
Testing data: 30%
Random state: 42
```
Stratification was used to maintain the distribution of the target variable between the training and testing datasets.

# 6. Feature Engineering
Three additional features were created.

AverageMonthlySpend
Calculated as:
```text
TotalCharges / tenure
```
For customers with zero tenure, MonthlyCharges is used instead.

This feature provides an estimate of the customer's average monthly spending based on their total charges and tenure.

TotalServices
This feature counts the number of active services among selected service-related variables.

It provides an indication of the extent of the customer's relationship with the company's services.

TenureGroup
Customers are grouped according to tenure:
```text
0–12 months       → New
13–24 months      → Developing
25–48 months      → Established
49+ months        → Loyal
```
This allows the model to capture possible non-linear relationships between customer tenure and churn.

# 7. Model Development
A Decision Tree Classifier was selected as the primary machine learning algorithm.

Multiple Decision Tree configurations were tested during model development.

The final configuration was selected based on the evaluation results observed on the validation/test workflow.

The final model is stored as part of the complete preprocessing and prediction pipeline.

# 8. Model Evaluation
The final model was evaluated using:

* Accuracy
* Precision
* Recall
* F1 Score
* Confusion Matrix

The model evaluation is documented in the Jupyter Notebook.

Recall is particularly relevant to the churn use case because false negatives represent customers who actually churned but were not identified by the model.

However, precision is also important because low precision may result in unnecessary retention interventions.

The appropriate balance between precision and recall depends on the relative business cost of missed churners and unnecessary interventions.

# 9. Model Interpretation
The Decision Tree was interpreted using:

* Feature importance
* Top feature analysis
* Decision Tree visualization

Feature importance identifies which variables contributed most to the trained model's decisions.

Feature importance should not be interpreted as causal evidence. A highly important feature indicates that it was useful to the trained model when making predictions, but does not establish that the feature itself causes customer churn.

# 10. Model Pipeline
The final model is stored as:
```text
model/churn_model.pkl
```
The saved object contains the complete machine learning pipeline:
```
Raw Customer Data
       |
       v
Feature Engineering
       |
       v
Missing Value Handling
       |
       v
Categorical Encoding
       |
       v
Decision Tree
       |
       v
Prediction
```
This ensures that the same preprocessing and feature engineering logic used during model training can be applied to new customer records.

# 11. REST API
A Flask REST API is provided in:
```text
app.py
```
The API provides the following endpoint:
```text
POST /predict
```
The endpoint accepts customer information in JSON format.

It returns:

* Churn prediction
* Churn probability

Example response:
```text
{
    "prediction": "Yes",
    "churn_probability": 0.82
}
```
The actual probability depends on the supplied customer information and trained model.

# 12. API Input
The API expects the following fields:
```text
gender
SeniorCitizen
Partner
Dependents
tenure
PhoneService
MultipleLines
InternetService
OnlineSecurity
OnlineBackup
DeviceProtection
TechSupport
StreamingTV
StreamingMovies
Contract
PaperlessBilling
PaymentMethod
MonthlyCharges
TotalCharges
```
# 13. Example API Request
A sample request is provided in:
```text
sample_request.json
```
Example:
```text
{
    "gender": "Female",
    "SeniorCitizen": 0,
    "Partner": "Yes",
    "Dependents": "No",
    "tenure": 5,
    "PhoneService": "Yes",
    "MultipleLines": "No",
    "InternetService": "Fiber optic",
    "OnlineSecurity": "No",
    "OnlineBackup": "No",
    "DeviceProtection": "No",
    "TechSupport": "No",
    "StreamingTV": "No",
    "StreamingMovies": "No",
    "Contract": "Month-to-month",
    "PaperlessBilling": "Yes",
    "PaymentMethod": "Electronic check",
    "MonthlyCharges": 70.70,
    "TotalCharges": 354.50
}
```
# 14. Example API Response
```text
{
    "prediction": "Yes",
    "churn_probability": 0.82
}
```
The returned probability is generated by the trained Decision Tree model and may differ depending on the input customer.

# 15. Installation
# Step 1: Clone or download the project
Open the project directory in VS Code.

# Step 2: Create a virtual environment
Windows:
```text
python -m venv .venv
```
# Step 3: Activate the virtual environment
Windows PowerShell:
```text
.venv\Scripts\Activate.ps1
```
Windows Command Prompt:
```text
.venv\Scripts\activate
```
# Step 4: Install dependencies
```text
pip install -r requirements.txt
```
# 16. Running the Jupyter Notebook
Install Jupyter if required:
```text
pip install notebook ipykernel
```
Register the environment:
```text
python -m ipykernel install --user --name churn-env --display-name "Python (Churn Project)"
```
Open:
```text
notebook/churn_analysis.ipynb
```
in VS Code.

Select the `Python (Churn Project)` kernel.

Run the notebook cells in order.

# 17. Running the Flask API
From the project root:
```text
python app.py
```
The API will run at:
```text
http://127.0.0.1:5000
```
Open the following URL in a browser to verify that the server is running:
```text
http://127.0.0.1:5000/
```
# 18. Testing the Prediction Endpoint
Using the provided sample request, send a POST request to:
```text
http://127.0.0.1:5000/predict
```
PowerShell example:
```text
Invoke-RestMethod `
  -Uri http://127.0.0.1:5000/predict `
  -Method Post `
  -ContentType "application/json" `
  -Body (Get-Content sample_request.json -Raw)
```
The API should return a response similar to:
```text
{
    "prediction": "Yes",
    "churn_probability": 0.82
}
```
# 19. Error Handling
The API validates incoming requests.

Examples of invalid input include:

* Missing required fields
* Invalid numeric values
* Invalid JSON request bodies

For invalid requests, the API returns an HTTP `400` response with information about the problem.

# 20. Project Files
customer_churn_project/
│
├── data/
│   └── WA_FnUseC_TelcoCustomerChurn.csv
│
├── notebook/
│   └── churn_analysis.ipynb
│
├── model/
│   ├── churn_model.pkl
│   └── decision_tree.png
│
├── feature_engineering.py
├── app.py
├── requirements.txt
├── README.md
└── sample_request.json

# 21. Technologies Used
* Python
* Pandas
* NumPy
* Scikit-learn
* Matplotlib
* Seaborn
* Joblib
* Flask
* Jupyter Notebook
* VS Code

# 22. Reproducibility
The train/test split uses:
```text
random_state=42
```
This ensures that the same split can be reproduced when the workflow is rerun with the same dataset and software configuration.

# 23. Conclusion
This project demonstrates a complete customer churn prediction workflow, from raw data preparation and exploratory analysis through machine learning, evaluation, interpretation, model serialization, and REST API deployment.

The resulting system can accept new customer information and return a predicted churn class together with its estimated churn probability.