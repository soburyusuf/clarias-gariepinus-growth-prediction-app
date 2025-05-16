import streamlit as st
import pandas as pd
import joblib

st.title("🐟 Clarias Fish Growth Predictor")
st.markdown("""
**Predict the final weight of your Clarias fish** based on feed composition and growth parameters.
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
    initial_mean_weight = st.slider(
        "Initial Weight (g)", 0.0, 10.0, 2.2, 0.1,
        help="Starting weight of the fish population"
    )
    mean_weight_gained = st.slider(
        "Weight Gained (g)", 0.0, 20.0, 4.0, 0.1,
        help="Current weight gain observed"
    )
    specific_growth_rate = st.slider(
        "Growth Rate (SGR)", 0.0, 20.0, 5.0, 0.1,
        help="Specific growth rate percentage"
    )

with col2:
    st.subheader("Feed Composition")
    # Linked feed percentage sliders
    commercial_feed = st.slider(
        "Commercial Feed (%)", 0.0, 1.0, 0.9, 0.01,
        format="%.2f",
        help="Percentage of commercial feed in diet"
    )
    spt_percentage = 1.0 - commercial_feed
    st.metric("SPT Percentage", f"{spt_percentage:.0%}", 
             help="Automatically calculated as 100% - Commercial Feed %")

    feed_conversion = st.slider(
        "Feed Conversion Rate", 0.0, 5.0, 0.4, 0.1,
        help="FCR: Feed required per unit weight gain"
    )

# Survival/Mortality Section
st.subheader("Health Metrics")
health_col1, health_col2 = st.columns(2)
with health_col1:
    mortality = st.slider(
        "Mortality Rate (%)", 0.0, 100.0, 60.0, 0.1,
        help="Percentage of population lost"
    )
with health_col2:
    survival = st.slider(
        "Survival Rate (%)", 0.0, 100.0, 40.0, 0.1,
        help="Percentage of population surviving"
    )

# Protein Source Selection
st.subheader("Protein Sources")
protein_type = st.selectbox(
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
    - **Trained on:** Historical growth data
    - **Features:** 10 growth parameters
    - **Algorithm:** Linear Regression
    """)
    st.markdown("## ⚠️ Requirements")
    st.markdown("Ensure `model.joblib` is in the same directory")

# Tooltip and validation
st.caption("💡 Tip: Adjust sliders to simulate different feeding scenarios")
