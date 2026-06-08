from pathlib import Path
import joblib
import pandas as pd
import streamlit as st

st.set_page_config(page_title="Term Deposit Subscription Predictor", layout="wide")

BASE_DIR = Path(__file__).resolve().parent
MODEL_PATH = BASE_DIR / "models" / "best_model.joblib"
PREPROCESSOR_PATH = BASE_DIR / "preprocessors" / "preprocessor.joblib"

@st.cache_resource
def load_artifacts():
    model = joblib.load(MODEL_PATH)
    preprocessor = joblib.load(PREPROCESSOR_PATH)
    return model, preprocessor

model, preprocessor = load_artifacts()

st.title("Term Deposit Subscription Predictor")

st.write("Enter client details below to predict whether the customer is likely to subscribe.")

with st.form("prediction_form"):
    col1, col2 = st.columns(2)

    with col1:
        age = st.number_input("Age", min_value=18, max_value=100, value=35)

        job = st.selectbox(
            "Job",
            [
                "admin.", "blue-collar", "entrepreneur", "housemaid", "management",
                "retired", "self-employed", "services", "student", "technician",
                "unemployed", "unknown"
            ]
        )

        marital = st.selectbox("Marital Status", ["divorced", "married", "single", "unknown"])

        education = st.selectbox(
            "Education",
            [
                "basic.4y", "basic.6y", "basic.9y", "high.school",
                "illiterate", "professional.course", "university.degree", "unknown"
            ]
        )

        default = st.selectbox("Credit in Default?", ["no", "yes", "unknown"])
        housing = st.selectbox("Housing Loan?", ["no", "yes", "unknown"])
        loan = st.selectbox("Personal Loan?", ["no", "yes", "unknown"])
        contact = st.selectbox("Contact Type", ["cellular", "telephone"])
        month = st.selectbox(
            "Last Contact Month",
            ["mar", "apr", "may", "jun", "jul", "aug", "sep", "oct", "nov", "dec"]
        )
        day_of_week = st.selectbox("Day of Week", ["mon", "tue", "wed", "thu", "fri"])

    with col2:
        duration = st.number_input("Call Duration (seconds)", min_value=0, max_value=5000, value=200)
        campaign = st.number_input("Campaign Contacts", min_value=1, max_value=100, value=1)
        pdays = st.number_input("Days Since Last Contact", min_value=0, max_value=999, value=999)
        previous = st.number_input("Previous Contacts", min_value=0, max_value=100, value=0)
        poutcome = st.selectbox("Previous Campaign Outcome", ["failure", "nonexistent", "success"])
        emp_var_rate = st.number_input("Employment Variation Rate", value=1.1, format="%.1f")
        cons_price_idx = st.number_input("Consumer Price Index", value=93.994, format="%.3f")
        cons_conf_idx = st.number_input("Consumer Confidence Index", value=-36.4, format="%.1f")
        euribor3m = st.number_input("Euribor 3 Month Rate", value=4.857, format="%.3f")
        nr_employed = st.number_input("Number of Employees", value=5191.0, format="%.1f")

    submitted = st.form_submit_button("Predict")

if submitted:
    input_df = pd.DataFrame({
        "age": [age],
        "job": [job],
        "marital": [marital],
        "education": [education],
        "default": [default],
        "housing": [housing],
        "loan": [loan],
        "contact": [contact],
        "month": [month],
        "day_of_week": [day_of_week],
        "duration": [duration],
        "campaign": [campaign],
        "pdays": [pdays],
        "previous": [previous],
        "poutcome": [poutcome],
        "emp.var.rate": [emp_var_rate],
        "cons.price.idx": [cons_price_idx],
        "cons.conf.idx": [cons_conf_idx],
        "euribor3m": [euribor3m],
        "nr.employed": [nr_employed]
    })

    try:
        input_preprocessed = preprocessor.transform(input_df)
        prediction = model.predict(input_preprocessed)[0]
        probability = model.predict_proba(input_preprocessed)[0][1]

        st.subheader("Prediction Result")

        if prediction == 1:
            st.success("Likely to Subscribe")
        else:
            st.error("Unlikely to Subscribe")

        st.metric("Subscription Probability", f"{probability:.2%}")

    except Exception as e:
        st.error(f"Prediction failed: {e}")