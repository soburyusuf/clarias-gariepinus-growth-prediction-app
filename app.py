import streamlit as st
import pandas as pd
import joblib 

model = joblib.load ('clarias_growth_prediction_model.joblib')
st.title("Clarias Growth Prediction")

# Collect inputs
initial_weight = st.number_input("Initial Mean Weight (g)", value=2.0)
spt_percentage = st.slider("SPT Percentage (decimal)", 0.0, 1.0, 0.2)
commercial_feed_percentage = st.slider("Commercial Feed Percentage (decimal)", 0.0, 1.0, 0.8)
single_cell_protein = st.selectbox("Single Cell Protein", ["Yes", "No"])
single_cell_protein_type = st.selectbox("Single Cell Protein Type", [
    "Citrus sinesis Peel", "Citrus sinesis Pulp", "Yam Peel", "Plantain Peel", "None"
])

# Prepare input DataFrame
input_df = pd.DataFrame([{
    'Initial Mean Weight (g)': initial_weight,
    'SPT Percentage': spt_percentage,
    'Commercial Feed Percentage': commercial_feed_percentage,
    'Single Cell Protein': single_cell_protein,
    'Single Cell Protein Type (SPT)': single_cell_protein_type
}])

# If your model requires preprocessing (encoding, scaling), apply it here or bundle it in a pipeline.

if st.button("Predict Final Mean Weight"):
    prediction = model.predict(input_df)[0]
    st.success(f"Predicted Final Mean Weight: {prediction:.2f} g")
    st.write("Note: The prediction is based on the provided input parameters and the trained model.")
else:
    st.write("Please enter the input parameters and click 'Predict Final Mean Weight' to see the prediction.")