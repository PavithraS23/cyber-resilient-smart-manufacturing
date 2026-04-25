import streamlit as st
import time
import random
from datetime import datetime

st.title("🔁 Autonomous Recovery System")

# Init
if "logs" not in st.session_state:
    st.session_state.logs = []

if "last_recovery_time" not in st.session_state:
    st.session_state.last_recovery_time = None

if "recovery_times" not in st.session_state:
    st.session_state.recovery_times = []

if st.session_state.get("status") == "Under Attack":

    if st.button("⚡ Initiate Self-Healing"):

        start_time = time.time()

        st.error("🚨 Cyberattack Confirmed")
        time.sleep(random.uniform(0.8, 1.5))

        st.write("🛑 Isolating Machine 2...")
        st.session_state.logs.append(
            f"{datetime.now().strftime('%H:%M:%S')} - 🛑 Machine Isolated"
        )
        time.sleep(random.uniform(0.8, 1.5))

        st.write("🧬 Activating Digital Twin...")
        st.session_state.twin = "Active"
        st.session_state.logs.append(
            f"{datetime.now().strftime('%H:%M:%S')} - 🧬 Digital Twin Activated"
        )
        time.sleep(random.uniform(0.8, 1.5))

        st.write("🔄 Restoring system...")
        st.session_state.status = "Recovered"
        st.session_state.machine2 = "Running"

        st.session_state.logs.append(
            f"{datetime.now().strftime('%H:%M:%S')} - ✅ System Recovered"
        )

        if "production" not in st.session_state:
            st.session_state.production = [100]

        st.session_state.production.append(100)

        time.sleep(random.uniform(0.8, 1.5))

        # Store timing
        total_time = time.time() - start_time
        st.session_state.last_recovery_time = total_time
        st.session_state.recovery_times.append(total_time)

        st.success("🏭 System Fully Restored")

else:
    st.info("System Secure")
