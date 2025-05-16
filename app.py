import streamlit as st
import pandas as pd
import joblib

st.title("🐟 Clarias Fish Growth Predictor")
st.markdown("""
**Predict the final mean weight of your Clarias fish** based on feed composition and growth parameters.
""")

# Load model with cache
@st.cache_resource
def load_model():
    return joblib.load("model.joblib")

model = load_model()

# Create two columns for better layout
col1, col2 = st.columns(2)

with col1:
    st.subheader("Growth Parameters")
    initial_mean_weight = st.number_input(
        "Initial Weight (g)", 0.0, 10.0, 2.2, 0.1,
        help="Starting weight of the fish population"
    )
    mean_weight_gained = st.number_input(
        "Weight Gained (g)", 0.0, 20.0, 4.0, 0.1,
        help="Current weight gain observed"
    )
    specific_growth_rate = st.number_input(
        "Growth Rate (SGR)", 0.0, 20.0, 5.0, 0.1,
        help="Specific growth rate percentage"
    )

with col2:
    st.subheader("Feed Composition")
    # Linked feed percentage sliders
    commercial_feed = spt_percentage = st.number_input("SPT Percentage (%)", 0.0, 100.0, 40.0, 0.1)
    commercial_feed_percentage = st.number_input("Commercial Feed Percentage (%)", 0.0, 100.0, 40.0, 0.1)

    

    feed_conversion = st.number_input(
        "Feed Conversion Rate", 0.0, 5.0, 0.4, 0.1,
        help="FCR: Feed required per unit weight gain"
    )

# Survival/Mortality Section
st.subheader("Health Metrics")
health_col1, health_col2 = st.columns(2)
with health_col1:
    mortality = st.number_input(
        "Mortality Rate (%)", 0.0, 100.0, 60.0, 0.1,
        help="Percentage of population lost"
    )
with health_col2:
    survival = st.number_input(
        "Survival Rate (%)", 0.0, 100.0, 40.0, 0.1,
        help="Percentage of population surviving"
    )

# Protein Source Selection
st.subheader("Protein Sources")
protein_type = st.radio(
    "Protein Type", 
    ["Citrus sinesis Peel", "Citrus sinesis Pulp", "Dioscorea rotundata Peel", "Non"],
    index=0,
    help="Type of single cell protein used"
)
use_protein = st.radio(
    "Use Single Cell Protein?",
    ["Yes", "No"],
    horizontal=True
)

# Prediction Button with Animation
if st.button("🎣 Calculate Final Weight", type="primary"):
    with st.spinner("Analyzing growth patterns..."):
        input_data = pd.DataFrame([{
            "Initial Mean Weight (g)": initial_mean_weight,
            "Mean Weight gained(g)": mean_weight_gained,
            "Specific Growth Rate (SGR)": specific_growth_rate,
            "Feed Conversion Rate (FCR)": feed_conversion,
            "Percentage Mortality (%PM)": mortality,
            "Percentage Survival (%PS)": survival,
            "Single Cell Protein": use_protein,
            "Single Cell Protein Type (SPT)": protein_type,
            "SPT Percentage": spt_percentage,
            "Commercial Feed Percentage": commercial_feed
        }])
        
        prediction = model.predict(input_data)
        st.balloons()
        st.success(f"**Predicted Final Mean Weight:** {prediction[0]:.2f} grams")
        st.progress(min(float(prediction[0]/100), 1.0))

# Sidebar with additional info
with st.sidebar:
    st.markdown("## 🧪 Model Info")
    st.markdown("""
    - **Trained on:** Unilorin zoology department Historical growth data
    - **Features:** 10 growth parameters
    - **Algorithm:** Linear Regression
    """)
   

# Tooltip and validation
st.caption("💡 Tip: Adjust sliders to simulate different feeding scenarios")
