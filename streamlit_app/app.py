import streamlit as st

st.set_page_config(
    page_title="Near-Earth Asteroid Analysis",
    page_icon="☄️",
    layout="wide",
)

st.title("🌌 Near-Earth Asteroid Analysis Dashboard")
st.sidebar.success("Select a page from the menu")

st.markdown("""
Welcome to the **Near-Earth Asteroid Analysis Dashboard**!  
Use the sidebar to explore different aspects of asteroid data:
- 🚀 Overview of all observations  
- ⚠️ Hazardous Asteroids  
- 💨 Velocity & Brightness Metrics  
""")