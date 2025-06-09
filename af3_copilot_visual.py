import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Page config
st.set_page_config(page_title="AlphaFold3 Co-Pilot", layout="centered")

# Title and intro
st.title("🧬 AlphaFold3 Co-Pilot for Crop Scientists")
st.markdown("""
Welcome to the **AlphaFold3 Co-Pilot**, a prototype to simulate how DeepMind’s protein folding tools could accelerate crop innovation.

This tool allows researchers to **work backward from a goal**, selecting:
- a crop of interest,
- the geography of cultivation,
- and a desired trait like shorter growing cycles or stress resistance.

Based on your choices, we show **mock predictions** of promising mutations with expected effects.
""")

# Sidebar selections
st.sidebar.header("🧪 Choose Inputs")
crop = st.sidebar.selectbox("1. Select a Crop", ["Rice", "Wheat"])
geo = st.sidebar.selectbox("2. Select a Geography", ["India", "Vietnam", "Ethiopia"])
goal = st.sidebar.selectbox("3. Select Desired Trait", ["Shorter Harvest Cycle", "Flood Resilience", "Disease Resistance"])

# Mock prediction data
results_data = {
    ("Rice", "India", "Shorter Harvest Cycle"): [
        ("Hd1 Mutation A", "Predicted 10-day earlier flowering", 85),
        ("Ehd1 Mutation C", "Predicted 7-day earlier flowering", 78),
    ],
    ("Wheat", "India", "Shorter Harvest Cycle"): [
        ("VRN1 Mutation B", "Predicted 12-day earlier flowering", 82),
    ],
    ("Rice", "Vietnam", "Flood Resilience"): [
        ("SUB1A Overexpression", "Improved flood tolerance (7 days)", 80),
    ],
    ("Wheat", "Ethiopia", "Disease Resistance"): [
        ("LR34 Mutation D", "Increased leaf rust resistance", 75),
    ]
}

# Display results
st.subheader("🔬 Prediction Results")

key = (crop, geo, goal)
if key in results_data:
    df = pd.DataFrame(results_data[key], columns=["Candidate Mutation", "Predicted Effect", "Confidence (%)"])
    st.dataframe(df, use_container_width=True)

    # Confidence bar chart
    st.markdown("#### 📊 Confidence Scores for Candidate Mutations")
    fig, ax = plt.subplots()
    ax.barh(df["Candidate Mutation"], df["Confidence (%)"], color="mediumseagreen")
    ax.set_xlabel("Confidence (%)")
    ax.set_xlim(0, 100)
    st.pyplot(fig)
else:
    st.warning("No predictions available for this combination yet. Please try another input.")

# Footer
st.markdown("---")
st.markdown("This is a conceptual prototype, not based on actual AlphaFold3 output.")
