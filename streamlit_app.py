import streamlit as st
import pandas as pd
import joblib
import numpy as np

# Load the trained model and columns
model = joblib.load("financial_inclusion_model.pkl")
model_columns = joblib.load("model_columns.pkl")

# Set page configuration
st.set_page_config(
    page_title="Financial Inclusion Prediction",
    page_icon="🏦",
    layout="wide"
)

# Title and description
st.title("🏦 Financial Inclusion in Africa Prediction")
st.markdown("""
This application predicts whether an individual is likely to have or use a bank account based on demographic information and financial service usage patterns.
""")

# Create input form
st.header("Enter Individual Information")

col1, col2 = st.columns(2)

with col1:
    # Country selection
    country = st.selectbox("Country", ["Kenya", "Rwanda", "Tanzania", "Uganda"])

    # Year selection
    year = st.selectbox("Year", [2016, 2017, 2018])

    # Location type
    location_type = st.selectbox("Location Type", ["Rural", "Urban"])

    # Cellphone access
    cellphone_access = st.selectbox("Cellphone Access", ["Yes", "No"])

    # Household size
    household_size = st.number_input("Household Size", min_value=1, max_value=20, value=5)

    # Age of respondent
    age_of_respondent = st.number_input("Age of Respondent", min_value=16, max_value=100, value=30)

with col2:
    # Gender
    gender_of_respondent = st.selectbox("Gender", ["Female", "Male"])

    # Relationship with head
    relationship_with_head = st.selectbox("Relationship with Head", 
                                        ["Head of Household", "Spouse", "Child", "Parent", "Other relative", "Other non-relatives"])

    # Marital status
    marital_status = st.selectbox("Marital Status", 
                                ["Married/Living together", "Divorced/Seperated", "Widowed", "Single/Never Married", "Dont know"])

    # Education level
    education_level = st.selectbox("Education Level", 
                                 ["No formal education", "Primary education", "Secondary education", 
                                  "Vocational/Specialised training", "Tertiary education", "Other/Dont know/RTA"])

    # Job type
    job_type = st.selectbox("Job Type", 
                          ["Self employed", "Government Dependent", "Formally employed Private", 
                           "Informally employed", "Formally employed Government", "Farming and Fishing", 
                           "Remittance Dependent", "Other Income", "Dont Know/Refuse to answer", "No Income"])

# Prediction button
if st.button("Predict Bank Account Usage", type="primary"):
    # Create input dataframe
    input_data = {
        'year': year,
        'household_size': household_size,
        'age_of_respondent': age_of_respondent
    }

    # Add categorical variables with one-hot encoding
    # Country
    for c in ['Rwanda', 'Tanzania', 'Uganda']:
        input_data[f'country_{c}'] = 1 if country == c else 0

    # Location type
    input_data['location_type_Urban'] = 1 if location_type == 'Urban' else 0

    # Cellphone access
    input_data['cellphone_access_Yes'] = 1 if cellphone_access == 'Yes' else 0

    # Gender
    input_data['gender_of_respondent_Male'] = 1 if gender_of_respondent == 'Male' else 0

    # Relationship with head
    for rel in ['Child', 'Head of Household', 'Other non-relatives', 'Other relative', 'Parent', 'Spouse']:
        input_data[f'relationship_with_head_{rel}'] = 1 if relationship_with_head == rel else 0

    # Marital status
    for status in ['Dont know', 'Married/Living together', 'Single/Never Married', 'Widowed']:
        input_data[f'marital_status_{status}'] = 1 if marital_status == status else 0

    # Education level
    for edu in ['Other/Dont know/RTA', 'Primary education', 'Secondary education', 'Tertiary education', 'Vocational/Specialised training']:
        input_data[f'education_level_{edu}'] = 1 if education_level == edu else 0

    # Job type
    for job in ['Dont Know/Refuse to answer', 'Farming and Fishing', 'Formally employed Government', 
                'Formally employed Private', 'Government Dependent', 'Informally employed', 
                'No Income', 'Other Income', 'Remittance Dependent', 'Self employed']:
        input_data[f'job_type_{job}'] = 1 if job_type == job else 0

    # Create DataFrame
    input_df = pd.DataFrame([input_data])

    # Ensure all model columns are present
    for col in model_columns:
        if col not in input_df.columns:
            input_df[col] = 0

    # Reorder columns to match model training
    input_df = input_df[model_columns]

    # Make prediction
    prediction = model.predict(input_df)[0]
    prediction_proba = model.predict_proba(input_df)[0]

    # Display results
    st.header("Prediction Results")

    if prediction == 1:
        st.success("✅ This individual is likely to have/use a bank account")
        st.metric("Probability of having a bank account", f"{prediction_proba[1]:.2%}")
    else:
        st.error("❌ This individual is unlikely to have/use a bank account")
        st.metric("Probability of having a bank account", f"{prediction_proba[1]:.2%}")

    # Show probability breakdown
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Probability: No Bank Account", f"{prediction_proba[0]:.2%}")
    with col2:
        st.metric("Probability: Has Bank Account", f"{prediction_proba[1]:.2%}")

# Add information about the model
st.sidebar.header("About the Model")
st.sidebar.info("""
This model was trained on demographic data from approximately 23,524 individuals across East Africa (Kenya, Rwanda, Tanzania, Uganda) to predict financial inclusion.

**Model Performance:**
- Accuracy: 86.16%
- The model uses Random Forest algorithm
- Features include demographic information, location, education, employment, and access to technology
""")

st.sidebar.header("Financial Inclusion")
st.sidebar.markdown("""
**Financial inclusion** means that individuals and businesses have access to useful and affordable financial products and services that meet their needs – transactions, payments, savings, credit and insurance – delivered in a responsible and sustainable way.
""")