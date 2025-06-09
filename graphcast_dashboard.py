import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium

# Set page configuration
st.set_page_config(page_title="GraphCast Smog Risk Dashboard", layout="wide")

# Title
st.title("🌫️ GraphCast-Powered Smog Risk Dashboard")
st.markdown("""
Use hyperlocal weather predictions to identify **high-risk pockets for smog events** due to crop burning in Northern India. 
Target decomposer spraying and enforcement efforts for **maximum impact**.
""")

# Mock data for targeted regions
risk_data = pd.DataFrame({
    "District": ["Ludhiana", "Karnal", "Varanasi", "Amritsar", "Bareilly", "Rohtak"],
    "State": ["Punjab", "Haryana", "Uttar Pradesh", "Punjab", "Uttar Pradesh", "Haryana"],
    "Latitude": [30.9, 29.7, 25.3, 31.6, 28.4, 28.9],
    "Longitude": [75.85, 76.98, 82.98, 74.86, 79.4, 76.57],
    "Predicted AQI": [450, 410, 390, 470, 350, 430],
    "Wind Speed (km/h)": [4, 3, 6, 2, 5, 3],
    "Inversion Risk": ["High", "Medium", "Low", "High", "Low", "Medium"],
    "Recommended Action": [
        "Deploy decomposers + enforce burn ban",
        "Monitor closely + early warnings",
        "No immediate action",
        "High priority: issue citizen alerts",
        "Public advisories only",
        "Targeted decomposer rollout"
    ]
})

# Create a map
st.subheader("🗺️ High-Risk Pockets Visualization")
m = folium.Map(location=[29.5, 77.0], zoom_start=6)
for _, row in risk_data.iterrows():
    color = "red" if row["Inversion Risk"] == "High" else "orange" if row["Inversion Risk"] == "Medium" else "green"
    folium.CircleMarker(
        location=[row["Latitude"], row["Longitude"]],
        radius=9,
        color=color,
        fill=True,
        fill_opacity=0.7,
        popup=(f"{row['District']}, {row['State']}<br>"
               f"AQI: {row['Predicted AQI']}<br>"
               f"Wind: {row['Wind Speed (km/h)']} km/h<br>"
               f"Inversion: {row['Inversion Risk']}<br>"
               f"Action: {row['Recommended Action']}")
    ).add_to(m)

st_data = st_folium(m, width=1000)

# Show risk table
st.subheader("📋 Risk Table and Recommendations")
st.dataframe(risk_data, use_container_width=True)

# Footer
st.markdown("---")
st.markdown("This dashboard uses simulated GraphCast data. In a real deployment, inputs would come from GraphCast weather forecasts and local crop burning detection tools.")
