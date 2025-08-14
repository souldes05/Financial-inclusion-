# Financial Inclusion in Africa Prediction

This project predicts whether an individual is likely to have or use a bank account based on demographic information and financial service usage patterns across East Africa.

## Dataset

The dataset contains demographic information and financial services usage data from approximately 23,524 individuals across East Africa (Kenya, Rwanda, Tanzania, Uganda). The goal is to predict which individuals are most likely to have or use a bank account.

## Features

- **Country**: Kenya, Rwanda, Tanzania, Uganda
- **Year**: 2016, 2017, 2018
- **Location Type**: Rural, Urban
- **Cellphone Access**: Yes, No
- **Household Size**: Number of people in household
- **Age of Respondent**: Age in years
- **Gender**: Male, Female
- **Relationship with Head**: Head of Household, Spouse, Child, Parent, Other relative, Other non-relatives
- **Marital Status**: Married/Living together, Divorced/Separated, Widowed, Single/Never Married, Don't know
- **Education Level**: No formal education, Primary education, Secondary education, Vocational/Specialised training, Tertiary education, Other/Don't know/RTA
- **Job Type**: Self employed, Government Dependent, Formally employed Private, Informally employed, Formally employed Government, Farming and Fishing, Remittance Dependent, Other Income, Don't Know/Refuse to answer, No Income

## Model Performance

- **Algorithm**: Random Forest Classifier
- **Accuracy**: 86.16%
- **Precision**: 91% (No Bank Account), 49% (Has Bank Account)
- **Recall**: 94% (No Bank Account), 38% (Has Bank Account)

## Files

- `streamlit_app.py`: Main Streamlit application
- `financial_inclusion_model.pkl`: Trained model
- `model_columns.pkl`: Feature columns used in training
- `requirements.txt`: Python dependencies

## How to Run

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Run the Streamlit app:
   ```bash
   streamlit run streamlit_app.py
   ```

3. Open your browser and navigate to the provided URL (usually http://localhost:8501)

## Deployment

This application is ready for deployment on Streamlit Cloud. Simply:

1. Push the code to a GitHub repository
2. Connect your GitHub account to Streamlit Cloud
3. Deploy the app by selecting the repository and main file (`streamlit_app.py`)

## About Financial Inclusion

Financial inclusion means that individuals and businesses have access to useful and affordable financial products and services that meet their needs – transactions, payments, savings, credit and insurance – delivered in a responsible and sustainable way.