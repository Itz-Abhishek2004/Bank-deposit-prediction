# Bank Term Deposit Subscription Prediction

A machine learning project that predicts whether a customer is likely to subscribe to a bank term deposit using demographic, financial, and campaign-related features. The underlying Bank Marketing dataset is widely described as data from direct marketing campaigns of a Portuguese banking institution conducted mainly through phone calls.

## Overview

This project combines exploratory data analysis, preprocessing, model building, evaluation, explainability, and deployment in one end-to-end workflow. The goal is not just to build a classifier, but to make the prediction usable through a Streamlit web application with saved model artifacts for inference.

## Problem Statement

Banks run marketing campaigns to convince customers to subscribe to term deposits, but contacting every customer is expensive and inefficient. This project aims to predict which customers are more likely to subscribe so campaigns can become more targeted and cost-effective.

## Objectives

- Perform exploratory data analysis to understand customer and campaign patterns.
- Clean and preprocess the dataset for machine learning.
- Train baseline and advanced classification models.
- Handle class imbalance where needed.
- Interpret the model using feature importance and SHAP.
- Deploy the final model using Streamlit for real-time prediction.

## Dataset

The dataset used in this project is based on the Bank Marketing dataset, which contains customer information and campaign interaction variables related to direct marketing efforts for term deposit subscription. Public descriptions of the dataset note that the task is to predict whether the client will subscribe to a term deposit.

### Target Variable

- `y` → Whether the client subscribed to a term deposit.

### Example Feature Groups

- Demographic features: age, job, marital status, education.
- Financial features: housing loan, personal loan, default history.
- Campaign features: contact type, month, duration, campaign count, previous outcome.
- Economic indicators: euribor rate, employment variation rate, consumer confidence, consumer price index.

## Tech Stack

- Python
- Pandas, NumPy
- Scikit-learn
- SHAP
- Matplotlib, Seaborn
- Joblib
- Streamlit
- Jupyter Notebook

## Project Workflow

### 1. Exploratory Data Analysis

The analysis phase focuses on understanding data distribution, missing or unknown values, class imbalance, and relationships between important features and the target variable.

### 2. Preprocessing

This stage includes feature preparation, encoding, scaling where necessary, and building a reusable preprocessing pipeline so inference stays consistent with training.

### 3. Baseline Modeling

Initial baseline models are trained to create a performance benchmark before moving to more advanced approaches.

### 4. Advanced Modeling

Advanced models are used to improve predictive performance, and imbalance-handling techniques such as SMOTE can be incorporated when needed.

### 5. Explainability

Feature importance and SHAP analysis help explain which factors contribute most to prediction outcomes.

### 6. Deployment

The final trained model and preprocessing pipeline are saved and connected to a Streamlit application for live predictions. Streamlit is commonly used to turn trained machine learning pipelines into simple interactive apps.

## Repository Structure

```bash
Bank-Term-Deposit-Subscription-Prediction/
│
├── app.py
├── README.md
├── requirements.txt
├── .gitignore
│
├── notebooks/
│   ├── eda.ipynb
│   ├── 02_Preprocessing_Baseline_Models.ipynb
│   └── 03_Advanced_Models_SMOTE_SHAP.ipynb
│
├── models/
│   └── best_model.joblib
│
├── preprocessors/
│   └── preprocessor.joblib
│
├── data/
│   └── bank.csv
│
└── outputs/
    └── feature_importance.csv
```

## Installation

Clone the repository:

```bash
git clone https://github.com/Itz-Abhishek2004/Bank-deposit-prediction.git
cd Bank-deposit-prediction
```

Create a virtual environment and activate it:

```bash
python -m venv venv
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Run the Streamlit App

```bash
streamlit run app.py
```

Streamlit apps are typically run from the project root using the `streamlit run` command against the app entry file.

## Model Artifacts

The repository stores the trained model and preprocessing pipeline separately using Joblib so predictions can be reproduced consistently in the application layer. This kind of serialized artifact workflow is common in deployed Scikit-learn projects.

- `models/best_model.joblib`
- `preprocessors/preprocessor.joblib`

## Features of the Project

- End-to-end machine learning pipeline.
- Clean repository structure.
- Separate notebooks for EDA, preprocessing, and advanced modeling.
- Saved preprocessing and model artifacts.
- Explainability support using SHAP.
- Streamlit app for interactive predictions.

## Future Improvements

- Add model performance comparison table in the README.
- Include screenshots of the Streamlit interface.
- Add deployment link if hosted online.
- Include confusion matrix, ROC curve, and final business insights.
- Add hyperparameter tuning summary.

## Learning Outcomes

This project demonstrates practical skills in data preprocessing, supervised learning, imbalance handling, model interpretation, and deployment of a machine learning application. Good machine learning project READMEs are expected to explain what the project does, why it is useful, and how to run it clearly for readers and recruiters.


