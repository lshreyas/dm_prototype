import streamlit as st
import pandas as pd

st.set_page_config(page_title="AlphaFold3 Co‑Pilot", layout="centered")

st.title("🧬 AlphaFold3 Co‑Pilot for Crop Scientists")
st.markdown("""
Work backwards from your goal — choose a state in India, select your crop and required trait, and explore how AlphaFold3 enables novel protein engineering designs.
""")

# Sidebar inputs
st.sidebar.header("🧪 Select Your Scenario")
state = st.sidebar.selectbox("1. Select a State", ["Punjab", "Uttar Pradesh", "Haryana"])
crop = st.sidebar.selectbox("2. Select Crop", ["Rice", "Wheat"])
goal = st.sidebar.selectbox("3. Select Trait", [
    "Shorter Harvest Cycle", "Disease Resistance", "Nitrogen Use Efficiency"
])

# Sample mutation data with AlphaFold enablement
results_data = {
    ("Punjab","Rice","Shorter Harvest Cycle"): [
        ("Hd1 Mut. A", "8‑day earlier flowering",
         "AlphaFold3 models Hd1 folding to ensure early expression."),
        ("Ehd1 Mut. C", "6‑day earlier", 
         "AF3 simulates interaction with RFT1 regulator."),
    ],
    ("Uttar Pradesh","Wheat","Disease Resistance"): [
        ("LR34 Mut. B", "Leaf rust protection",
         "AF3 assesses structural stability of resistance protein."),
        ("Pm3a Var X", "Powdery mildew defense",
         "AF3 models direct binding to pathogen protein."),
    ],
    ("Haryana","Rice","Nitrogen Use Efficiency"): [
        ("NRT1.1 Mut.", "Better nitrogen uptake",
         "AF3 evaluates transporter membrane stability."),
        ("GLN1 OE", "Improved nitrogen assimilation",
         "AF3 simulates enzyme‑substrate catalytic interface."),
    ],
}

st.subheader("🔬 Predicted Mutations and AlphaFold3 Insights")
key = (state, crop, goal)
if key in results_data:
    df = pd.DataFrame(results_data[key], columns=[
        "Candidate Mutation", "Predicted Effect", "AlphaFold3 Role"
    ])
    st.dataframe(df, use_container_width=True)
else:
    st.warning("No data available yet—try a different combination.")

st.markdown("---")
st.markdown("### 🧪 AlphaFold Structure Examples")
st.markdown("""
AlphaFold3 generates high‑confidence 3D protein structures crucial for:
- Predicting impact of mutations
- Validating stability and interactions
- Selecting viable agricultural protein targets
""")
st.image([
    "https://via.placeholder.com/300?text=AlphaFold+Structure+1",
    "https://via.placeholder.com/300?text=AlphaFold+Structure+2"
], caption=["Example folding of Hd1", "Transporter protein structure modeled by AF3"],
width=300)

st.markdown("---")
st.markdown("📌 **Note**: This is a conceptual prototype for illustration — outputs are not derived from actual AlphaFold3 runs.")
