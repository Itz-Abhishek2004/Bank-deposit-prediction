# Bank Term Deposit Subscription Prediction

This project predicts whether a bank client is likely to subscribe to a term deposit using machine learning and a Streamlit web application. The project brief expects a binary classification solution, reusable preprocessing pipeline, evaluation metrics, explainability, and a user-facing dashboard.[1]

## Problem Statement

Banks often struggle to identify which clients are most likely to subscribe to a term deposit offer. The main objective of this project is to build a binary classification model that predicts customer subscription using demographic, financial, and campaign-related features.[1]

## Business Objective

This project supports targeted marketing, cost optimization, customer prioritization, and better campaign decision-making. The brief also frames the work as a predictive analytics problem for the banking and financial services domain.[1]

## Dataset

The dataset used in this project is based on the Bank Marketing dataset, with demographic, financial, and campaign-related variables and an imbalanced subscription target.[1]

## Project Workflow

The repository follows a practical end-to-end machine learning workflow:

- Exploratory data analysis in notebooks.
- Data preprocessing and baseline model development.
- Advanced modeling with class imbalance handling and explainability.
- Model serialization using Joblib.
- Streamlit application for live prediction.

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

## Expected Deliverables

According to the project brief, the expected deliverables include a cleaned dataset, modeling notebooks, preprocessing and modeling pipeline, leaderboard-style model comparison, explainability analysis, deployed model or dashboard, and final documentation with business takeaways.[1]

## Evaluation Metrics

The required evaluation metrics in the brief are:

- Accuracy[1]
- Precision[1]
- Recall[1]
- F1-Score[1]
- ROC-AUC[1]

## Explainability

The brief specifically asks for feature importance and SHAP-based interpretability so that the factors influencing subscription decisions can be analyzed clearly.[1]

## Streamlit Application

The repository includes a Streamlit application that allows users to enter customer details and generate a live subscription prediction. The deployment component is explicitly included in the project expectations, while AWS deployment is described as optional.[1]

## How to Run

1. Clone the repository.
2. Create and activate a virtual environment.
3. Install dependencies using `requirements.txt`.
4. Run the Streamlit app:

```bash
streamlit run app.py
```

## Requirements

Install the dependencies with:

```bash
pip install -r requirements.txt
```

## Project Highlights

- End-to-end binary classification workflow for banking analytics.[1]
- Reusable preprocessing and modeling pipeline.[1]
- Business-focused evaluation and explainability.[1]
- Streamlit-based prediction interface.[1]

## Notes

The project brief emphasizes modular code, transparency in assumptions, avoidance of data leakage, and documentation of feature and modeling decisions.[1]── 03_Advanced_Models_SMOTE_SHAP.ipynb
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

## Submission Readiness

A project with the above structure, proper metrics, documented explainability, and a working Streamlit app would align well with the stated brief. The most important final check is ensuring that the notebooks, serialized artifacts, README, and report all match the claims made in the project summary.[cite:960]
