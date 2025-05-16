import streamlit as st
import numpy as np
import joblib

# Load your trained model
@st.cache_resource
def load_model():
    # Update the filename to match your saved model
    return joblib.load("model.joblib")

model = load_model()

st.title("Clarias Fish Final Mean Weight Prediction")

st.markdown("""
This app predicts the **Final Mean Weight (g)** of Clarias fish based on feed composition and growth parameters.
""")

# Input fields for all features used in the model
initial_mean_weight = st.number_input("Initial Mean Weight (g)", min_value=0.0, value=2.2, step=0.01)
mean_weight_gained = st.number_input("Mean Weight Gained (g)", min_value=0.0, value=4.0, step=0.01)
specific_growth_rate = st.number_input("Specific Growth Rate (SGR)", min_value=0.0, value=5.0, step=0.01)
feed_conversion_rate = st.number_input("Feed Conversion Rate (FCR)", min_value=0.0, value=0.4, step=0.01)
percentage_mortality = st.number_input("Percentage Mortality (%PM)", min_value=0.0, max_value=100.0, value=60.0, step=0.1)
percentage_survival = st.number_input("Percentage Survival (%PS)", min_value=0.0, max_value=100.0, value=40.0, step=0.1)
single_cell_protein = st.selectbox("Single Cell Protein", ["Yes", "No"])
single_cell_protein_type = st.selectbox(
    "Single Cell Protein Type (SPT)",
    ["Citrus sinesis Peel", "Citrus sinesis Pulp", "Other"]
)
spt_percentage = st.slider("SPT Percentage(decimal)", 0.0, 1.0, 0.8)
commercial_feed_percentage = st.slider("Commercial Feed Percentage (decimal)", 0.0, 1.0, 0.8)

# Prepare input for prediction
# Adjust this order and preprocessing to match your model pipeline
input_data = np.array([
    initial_mean_weight,
    mean_weight_gained,
    specific_growth_rate,
    feed_conversion_rate,
    percentage_mortality,
    percentage_survival,
    1 if single_cell_protein == "Yes" else 0,
    1 if single_cell_protein_type == "Citrus sinesis Peel" else (2 if single_cell_protein_type == "Citrus sinesis Pulp" else 0),
    spt_percentage,
    commercial_feed_percentage
]).reshape(1, -1)

if st.button("Predict Final Mean Weight"):
    prediction = model.predict(input_data)
    st.success(f"Predicted Final Mean Weight: **{prediction[0]:.2f} g**")

st.markdown("---")
st.markdown("**Note:** Ensure the model file (`model.joblib`) is in the same directory as this app.")
