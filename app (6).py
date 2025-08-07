
import joblib
import streamlit as st

model = joblib.load("bank_account_model.pkl")
model_columns = joblib.load("model_columns.pkl")

st.title("💳 Financial Inclusion in Africa - Bank Account Prediction")
st.write("Fill in the details below to predict if an individual is likely to have a bank account.")
