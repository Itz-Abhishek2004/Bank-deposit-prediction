Bank Term Deposit Subscription Prediction
This project predicts whether a bank client is likely to subscribe to a term deposit using machine learning and a Streamlit web application. The project brief expects a binary classification solution, reusable preprocessing pipeline, evaluation metrics, explainability, and a user-facing dashboard.

Problem Statement
Banks often struggle to identify which clients are most likely to subscribe to a term deposit offer. The main objective of this project is to build a binary classification model that predicts customer subscription using demographic, financial, and campaign-related features.

Business Objective
This project supports targeted marketing, cost optimization, customer prioritization, and better campaign decision-making. The brief also frames the work as a predictive analytics problem for the banking and financial services domain.

Dataset
The dataset used in this project is based on the Bank Marketing dataset, with demographic, financial, and campaign-related variables and an imbalanced subscription target.

Project Workflow
The repository follows a practical end-to-end machine learning workflow:

Exploratory data analysis in notebooks.

Data preprocessing and baseline model development.

Advanced modeling with class imbalance handling and explainability.

Model serialization using Joblib.

Streamlit application for live prediction.

Repository Structure
bash
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
Expected Deliverables
According to the project brief, the expected deliverables include a cleaned dataset, modeling notebooks, preprocessing and modeling pipeline, leaderboard-style model comparison, explainability analysis, deployed model or dashboard, and final documentation with business takeaways.

Evaluation Metrics
The required evaluation metrics in the brief are:

Accuracy

Precision

Recall

F1-Score

ROC-AUC

Explainability
The brief specifically asks for feature importance and SHAP-based interpretability so that the factors influencing subscription decisions can be analyzed clearly.

Streamlit Application
The repository includes a Streamlit application that allows users to enter customer details and generate a live subscription prediction. The deployment component is explicitly included in the project expectations, while AWS deployment is described as optional.

How to Run
Clone the repository.

Create and activate a virtual environment.

Install dependencies using requirements.txt.

Run the Streamlit app:

bash
streamlit run app.py
Requirements
Install the dependencies with:

bash
pip install -r requirements.txt
Project Highlights
End-to-end binary classification workflow for banking analytics.

Reusable preprocessing and modeling pipeline.

Business-focused evaluation and explainability.

Streamlit-based prediction interface.

Notes
The project brief emphasizes modular code, transparency in assumptions, avoidance of data leakage, and documentation of feature and modeling decisions