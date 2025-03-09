import streamlit as st
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler, LabelEncoder, OneHotEncoder
import pickle
from tensorflow.keras.models import load_model # type: ignore

# Load the trained model
model = load_model('customer_churn_model.h5')

# Load the label encoder, one hot encoder and scaler
with open('gender_label_encoder.pkl', 'rb') as file:
    gender_label_encoder = pickle.load(file)

with open('geography_one_hot_encoder.pkl', 'rb') as file:
    geography_one_hot_encoder = pickle.load(file)

with open('scaler.pkl', 'rb') as file:
    scaler = pickle.load(file)

# Streamlit app
st.title('Customer Churn Prediction')

# User input
geography = st.selectbox('Geography', geography_one_hot_encoder.categories_[0])
gender = st.selectbox('Gender', gender_label_encoder.classes_)
age = st.slider('Age', 18, 100)
balance = st.number_input('Balance')
credit_score = st.number_input('Credit Score')
estimated_salary = st.number_input('Estimated Salary')
tenure = st.slider('Tenure', 0, 10)
num_of_products = st.slider('Number of Products', 1, 4)
has_credit_card = st.selectbox('Has Credit Card?', ['Yes', 'No'])
has_credit_card = 1 if has_credit_card == 'Yes' else 0
is_active_member = st.selectbox('Is Active Member?', ['Yes', 'No'])
is_active_member = 1 if is_active_member == 'Yes' else 0

# Preprocess the user input
input_data = pd.DataFrame({
    'CreditScore': [credit_score],
    'Gender': [gender_label_encoder.transform([gender])[0]],
    'Age': [age],
    'Tenure': [tenure],
    'Balance': [balance],
    'NumOfProducts': [num_of_products],
    'HasCrCard': [has_credit_card],
    'IsActiveMember': [is_active_member],
    'EstimatedSalary': [estimated_salary],
})

# Encode geography
geography_encoded = geography_one_hot_encoder.transform([[geography]]).toarray()
geography_encoded_df = pd.DataFrame(geography_encoded, columns=geography_one_hot_encoder.get_feature_names_out(['Geography']))

# Concatenate the input data and the encoded geography
input_data = pd.concat([input_data.reset_index(drop=True), geography_encoded_df], axis=1)

# Scale the input data
input_data_scaled = scaler.transform(input_data)

# Predict the churn probability
churn_probability = model.predict(input_data_scaled)[0][0]

# Display the churn probability
if churn_probability > 0.5:
    st.write('The customer is likely to churn with a probability of', round(churn_probability * 100, 3), '%')
else:
    st.write('The customer is not likely to churn with a probability of', round((1 - churn_probability) * 100, 3), '%')