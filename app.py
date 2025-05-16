import streamlit as st
import pandas as pd
import joblib

st.title("Clarias Fish Final Mean Weight Prediction")

st.markdown("""
This app predicts the **Final Mean Weight (g)** of Clarias fish based on feed composition and growth parameters.
The model pipeline includes numeric imputation, scaling, and one-hot encoding for categorical features.
""")

@st.cache_resource
def load_model():
    return joblib.load("model.joblib")

model = load_model()

# Input widgets for features
initial_mean_weight = st.number_input("Initial Mean Weight (g)", min_value=0.0, value=2.2, step=0.01)
mean_weight_gained = st.number_input("Mean Weight gained (g)", min_value=0.0, value=4.0, step=0.01)
specific_growth_rate = st.number_input("Specific Growth Rate (SGR)", min_value=0.0, value=5.0, step=0.01)
feed_conversion_rate = st.number_input("Feed Conversion Rate (FCR)", min_value=0.0, value=0.4, step=0.01)
percentage_mortality = st.number_input("Percentage Mortality (%PM)", min_value=0.0, max_value=100.0, value=60.0, step=0.1)
percentage_survival = st.number_input("Percentage Survival (%PS)", min_value=0.0, max_value=100.0, value=40.0, step=0.1)
single_cell_protein = st.selectbox("Single Cell Protein", ["Yes", "No"])
single_cell_protein_type = st.selectbox(
    "Single Cell Protein Type (SPT)",
    ["Citrus sinesis Peel", "Citrus sinesis Pulp"]
)
spt_percentage = st.number_input("SPT Percentage", min_value=0.0, max_value=1.0, value=0.1, step=0.01)
commercial_feed_percentage = st.number_input("Commercial Feed Percentage", min_value=0.0, max_value=1.0, value=0.9, step=0.01)

# Prepare input DataFrame matching training features
input_df = pd.DataFrame([{
    "Initial Mean Weight (g)": initial_mean_weight,
    "Mean Weight gained(g)": mean_weight_gained,
    "Specific Growth Rate (SGR)": specific_growth_rate,
    "Feed Conversion Rate (FCR)": feed_conversion_rate,
    "Percentage Mortality (%PM)": percentage_mortality,
    "Percentage Survival (%PS)": percentage_survival,
    "Single Cell Protein": single_cell_protein,
    "Single Cell Protein Type (SPT)": single_cell_protein_type,
    "SPT Percentage": spt_percentage,
    "Commercial Feed Percentage": commercial_feed_percentage
}])

if st.button("Predict Final Mean Weight"):
    prediction = model.predict(input_df)
    st.success(f"Predicted Final Mean Weight: **{prediction[0]:.2f} g**")

st.markdown("---")
st.markdown("Make sure the `model.joblib` file is in the same directory as this app.")
