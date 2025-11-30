import streamlit as st
import plotly.express as px
from neas.data import get_data
from neas.transforms import kpi_overview

st.title("🚀 Asteroids Overview")

df = get_data()
kpi = kpi_overview(df)

# KPI cards
c1, c2, c3, c4 = st.columns(4)
c1.metric("Total Observations", f"{kpi['observations']:,}")
c2.metric("Total Asteroids", f"{kpi['asteroids']:,}")
c3.metric("Potentially Hazardous", f"{kpi['potentially_hazardous']:,}")
c4.metric("Confirmed Hazardous", f"{kpi['hazardous']:,}")

# Charts
col1, col2 = st.columns(2)

with col1:
    fig1 = px.pie(df, names="size_class", title="Asteroids by Diameter")
    st.plotly_chart(fig1, use_container_width=True)

with col2:
    fig2 = px.scatter(
        df,
        x="closest_approach_km",
        y="estimated_diameter_km",
        color="hazardous",
        title="Proximity vs Diameter",
        labels={"closest_approach_km": "Closest Approach (km)", "estimated_diameter_km": "Diameter (km)"}
    )
    st.plotly_chart(fig2, use_container_width=True)
