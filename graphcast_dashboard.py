import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium

# Set page configuration
st.set_page_config(page_title="GraphCast Smog Risk Dashboard", layout="wide")

# Title and intro
st.title("🌫️ GraphCast Smog Risk Targeting Tool")
st.markdown("""
Use this interactive dashboard to **identify and prioritize districts in North India** with high smog risk due to crop burning. 
Forecasted air quality, wind patterns, and atmospheric inversion risks help optimize **decomposer rollout, enforcement, and public alerts**.
""")

# Mock data with extended info
risk_data = pd.DataFrame({
    "District": ["Ludhiana", "Karnal", "Varanasi", "Amritsar", "Bareilly", "Rohtak", "Jalandhar", "Meerut"],
    "State": ["Punjab", "Haryana", "Uttar Pradesh", "Punjab", "Uttar Pradesh", "Haryana", "Punjab", "Uttar Pradesh"],
    "Latitude": [30.9, 29.7, 25.3, 31.6, 28.4, 28.9, 31.3, 28.98],
    "Longitude": [75.85, 76.98, 82.98, 74.86, 79.4, 76.57, 75.57, 77.7],
    "Predicted AQI": [450, 410, 390, 470, 350, 430, 420, 400],
    "Wind Speed (km/h)": [4, 3, 6, 2, 5, 3, 2, 4],
    "Humidity (%)": [58, 65, 70, 60, 75, 68, 62, 66],
    "Inversion Risk": ["High", "Medium", "Low", "High", "Low", "Medium", "High", "Medium"],
    "Burn Events Detected": [27, 22, 5, 33, 8, 19, 30, 15],
    "Recommended Action": [
        "Deploy decomposers + enforce ban",
        "Monitor closely + send alerts",
        "No immediate action",
        "Issue high-priority public health warning",
        "Advisories for at-risk populations",
        "Targeted decomposer rollout",
        "Maximize enforcement + pre-emptive spraying",
        "Early-warning nudges to farmers"
    ],
    "Forecast Date": ["2025-06-10", "2025-06-10", "2025-06-10", "2025-06-10", "2025-06-10", "2025-06-10", "2025-06-10", "2025-06-10"]
})

# Interactive filters
st.sidebar.header("🔍 Filter Districts")
aqi_thresh = st.sidebar.slider("Minimum AQI", 300, 500, 400)
burn_event_thresh = st.sidebar.slider("Minimum Burn Events Detected", 0, 40, 10)
inv_filter = st.sidebar.multiselect("Inversion Risk Levels", ["High", "Medium", "Low"], default=["High", "Medium"])

# Time slider: Forecast Date selection
st.sidebar.subheader("🗓️ Select Forecast Date")
forecast_date = st.sidebar.date_input("Choose forecast date", pd.to_datetime("2025-06-10"))

# Filter data based on selection
filtered_data = risk_data[
    (risk_data["Predicted AQI"] >= aqi_thresh) &
    (risk_data["Burn Events Detected"] >= burn_event_thresh) &
    (risk_data["Inversion Risk"].isin(inv_filter)) &
    (risk_data["Forecast Date"] == str(forecast_date))
]

# Show filtered map
st.subheader("🗺️ Priority Intervention Zones")
m = folium.Map(location=[29.5, 77.0], zoom_start=6)
for _, row in filtered_data.iterrows():
    color = "red" if row["Inversion Risk"] == "High" else "orange" if row["Inversion Risk"] == "Medium" else "green"
    folium.CircleMarker(
        location=[row["Latitude"], row["Longitude"]],
        radius=10,
        color=color,
        fill=True,
        fill_opacity=0.8,
        popup=(f"<b>{row['District']}, {row['State']}</b><br>"
               f"AQI: {row['Predicted AQI']}<br>"
               f"Wind: {row['Wind Speed (km/h)']} km/h<br>"
               f"Humidity: {row['Humidity (%)']}%<br>"
               f"Inversion: {row['Inversion Risk']}<br>"
               f"Burn Events: {row['Burn Events Detected']}<br>"
               f"<i>{row['Recommended Action']}</i>")
    ).add_to(m)

st_data = st_folium(m, width=1000)

# Display filtered table
st.subheader("📋 Targeted Districts and Recommendations")
st.dataframe(filtered_data.reset_index(drop=True), use_container_width=True)

# Summary statistics
st.subheader("📈 Summary Statistics")
st.markdown(f"**Number of Districts Matching Criteria:** {len(filtered_data)}")
if len(filtered_data) > 0:
    avg_aqi = filtered_data['Predicted AQI'].mean()
    avg_burn = filtered_data['Burn Events Detected'].mean()
    st.markdown(f"- **Average AQI:** {avg_aqi:.1f}")
    st.markdown(f"- **Average Burn Events:** {avg_burn:.1f}")

# Footer
st.markdown("---")
st.markdown("⚠️ This is a conceptual demo using mock data. In production, data would be sourced from GraphCast forecasts and satellite burn event detection systems.")
