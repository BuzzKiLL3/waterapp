import streamlit as st
import random
import time

st.set_page_config(page_title="Water Tank Monitor", page_icon="💧", layout="centered")

# Initialize session state
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False
if 'sensor_id' not in st.session_state:
    st.session_state.sensor_id = None
if 'sensor_value' not in st.session_state:
    st.session_state.sensor_value = random.randint(0, 100)

def simulate_sensor_value():
    """Simulate fetching new sensor data"""
    st.session_state.sensor_value = random.randint(0, 100)

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

# Sensor ID input
elif not st.session_state.sensor_id:
    st.title("🛰️ Connect Sensor")
    sensor_id = st.text_input("Enter Sensor ID")
    if st.button("Connect Sensor"):
        if sensor_id:
            st.session_state.sensor_id = sensor_id
            simulate_sensor_value()
        else:
            st.error("Sensor ID cannot be empty.")

# Water Tank UI
else:
    st.title("💧 Water Tank Live Visualization")
    st.markdown(f"**Sensor ID**: `{st.session_state.sensor_id}`")
    st.markdown("---")

    sensor_val = st.session_state.sensor_value
    tank_height = 300  # Just for scale
    fill_percent = (sensor_val / 100)

    # Display tank
    st.markdown(f"""
        <div style="width: 150px; height: {tank_height}px; border: 4px solid #2563eb;
                    border-bottom-left-radius: 80px; border-bottom-right-radius: 80px;
                    background: #dbeafe; margin: auto; position: relative; overflow: hidden;">
            <div style="position: absolute; bottom: 0; width: 100%; height: {int(fill_percent * tank_height)}px;
                        background-color: #3b82f6; transition: height 1s;"></div>
            <div style="position: absolute; bottom: 10px; width: 100%; text-align: center;
                        color: white; font-weight: bold; font-size: 1.25rem;">
                {sensor_val}%
            </div>
        </div>
    """, unsafe_allow_html=True)

    st.markdown("---")
    if st.button("🔄 Refresh Sensor Data"):
        simulate_sensor_value()
        st.experimental_rerun()
