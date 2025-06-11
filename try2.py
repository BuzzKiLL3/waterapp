import streamlit as st
import random

st.set_page_config(page_title="Water Tank Monitor", page_icon="💧", layout="wide")

# Initialize session state
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False
if 'sensor_connected' not in st.session_state:
    st.session_state.sensor_connected = False
if 'sensor_values' not in st.session_state:
    st.session_state.sensor_values = {
        "Tank 1": random.randint(0, 100),
        "Tank 2": random.randint(0, 100),
        "Tank 3": random.randint(0, 100)
    }

def simulate_sensor_values():
    for tank in st.session_state.sensor_values:
        st.session_state.sensor_values[tank] = random.randint(0, 100)

# Login page
if not st.session_state.logged_in:
    st.title("🔐 Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Sign In"):
        if username and password:
            st.session_state.logged_in = True
        else:
            st.error("Enter both username and password.")

# Sensor connection page
elif not st.session_state.sensor_connected:
    st.title("🛰️ Connect to Sensors")
    sensor_id = st.text_input("Enter Sensor System ID")
    if st.button("Connect"):
        if sensor_id:
            st.session_state.sensor_connected = True
            simulate_sensor_values()
        else:
            st.error("Sensor ID cannot be empty.")

# Dashboard with multiple tanks
else:
    st.title("💧 Water Tank Monitoring Dashboard")
    st.markdown("---")

    col1, col2, col3 = st.columns(3)
    for i, (tank_name, value) in enumerate(st.session_state.sensor_values.items()):
        fill_percent = value / 100
        tank_height = 250

        tank_html = f"""
            <div style="width: 130px; height: {tank_height}px; border: 4px solid #2563eb;
                        border-bottom-left-radius: 80px; border-bottom-right-radius: 80px;
                        background: #dbeafe; margin: auto; position: relative; overflow: hidden;">
                <div style="position: absolute; bottom: 0; width: 100%; height: {int(fill_percent * tank_height)}px;
                            background-color: #3b82f6; transition: height 1s;"></div>
                <div style="position: absolute; bottom: 10px; width: 100%; text-align: center;
                            color: white; font-weight: bold; font-size: 1.25rem;">
                    {value}%
                </div>
            </div>
        """

        with [col1, col2, col3][i]:
            st.markdown(f"### {tank_name}")
            st.markdown(tank_html, unsafe_allow_html=True)

    st.markdown("---")
    if st.button("🔄 Refresh All Tanks"):
        simulate_sensor_values()
        st.experimental_rerun()
