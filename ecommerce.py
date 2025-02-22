import streamlit as st
import joblib
import numpy as np 
import urllib.request
import warnings
warnings.filterwarnings("ignore")
import base64

def set_page_style():
    st.markdown(
        """
        <style>
        /* Set full-page background */
        .stApp {
            background: linear-gradient(135deg,rgb(194, 218, 148),rgb(233, 210, 163));
            font-family: 'Poppins', sans-serif;
            background-attachment: fixed;
            background-size: cover;
            color: black;
            font-weight: bold;
            font-family: 'Poppins', sans-serif;
        }

        /* Change header font */
        .stTitle {
            font-size: 36px !important;
            font-weight: bold;
            color:rgb(242, 9, 9) !important;
            text-align: center;
        }

        /* Style buttons */
        .stButton>button {
            background:rgb(37, 211, 46);
            font-family: 'Lobster', cursive;
            color: white;
            font-size: 20px;
            padding: 10px 24px;
            border-radius: 10px;
            font-weight: bold;
            border: none;
            transition: 0.3s ease-in-out;
        }
        .stButton>button:hover {
            background:rgb(152, 232, 125);
            transform: scale(1.1);
        }

        /* Style input boxes */
        .stTextInput, .stNumberInput, .stSlider {
            background: rgba(68, 154, 185, 0.72);
            font-family: 'Lobster', cursive;
            border-radius: 10px;
            padding: 10px;
        }

        /* Add box shadow to widgets */
        .stTextInput>div, .stNumberInput>div, .stSlider>div {
            box-shadow: 0px 4px 10px rgba(23, 8, 96, 0.89);
        }
        </style>
        """,
        unsafe_allow_html=True
    )

set_page_style()



# Load the trained model
model = joblib.load("ecommercemodel.pkl")

st.title("Ecommerce Customer Yearly Amount Spending Prediction")

st.write("""Enter Customer Details:""")

# User input fields
avg_session_length = st.number_input("Avg. Session Length (minutes)", min_value=0.0)
time_on_app = st.number_input("Time on App (minutes)", min_value=0.0)
time_on_website = st.number_input("Time on Website (minutes)", min_value=0.0)
length_of_membership = st.number_input("Length of Membership (years)", min_value=0.0)

# Predict button
if st.button("Predict"):
    # Prepare input data
    input_data = np.array([[avg_session_length, time_on_app, time_on_website, length_of_membership]])
    
    # Make prediction
    prediction = model.predict(input_data)
    
    # Display prediction
    st.write(f"Predicted Yearly Amount Spent: ${prediction[0]:.2f}")