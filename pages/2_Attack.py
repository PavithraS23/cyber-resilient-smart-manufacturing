import streamlit as st
import time
from datetime import datetime

st.title("🚨 Cyberattack Simulation")

# Init logs
if "logs" not in st.session_state:
    st.session_state.logs = []

if st.button("🔥 Launch Ransomware Attack"):

    st.error("⚠️ Ransomware Detected!")
    time.sleep(1)

    st.write("🔍 Analyzing system breach...")
    time.sleep(1)

    st.write("🚨 Unauthorized encryption activity detected")
    time.sleep(1)

    st.write("📉 Production dropping...")
    time.sleep(1)

    # Update system
    st.session_state.status = "Under Attack"
    st.session_state.machine2 = "Compromised"

    # Logs
    st.session_state.logs.append(
        f"{datetime.now().strftime('%H:%M:%S')} - ⚠️ Ransomware Attack Detected"
    )
    st.session_state.logs.append(
        f"{datetime.now().strftime('%H:%M:%S')} - 🚨 System Breach Identified"
    )
    st.session_state.logs.append(
        f"{datetime.now().strftime('%H:%M:%S')} - 📉 Production Dropped"
    )

    # Production drop
    if "production" not in st.session_state:
        st.session_state.production = [100]

    st.session_state.production.append(40)

    st.error("🚨 SYSTEM UNDER ATTACK")
