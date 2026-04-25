import streamlit as st
import random
import pandas as pd

st.title("📊 Factory Command Center")

# ✅ INIT
if "status" not in st.session_state:
    st.session_state.status = "Normal"
    st.session_state.machine2 = "Running"
    st.session_state.twin = "Standby"
    st.session_state.logs = []
    st.session_state.production = [100]
    st.session_state.last_recovery_time = None
    st.session_state.recovery_times = []

# 🔹 Threat level (visual only)
if st.session_state.status == "Under Attack":
    threat = random.randint(70, 95)
elif st.session_state.status == "Recovered":
    threat = random.randint(5, 20)
else:
    threat = random.randint(1, 15)

# 🔹 KPI
c1, c2, c3, c4 = st.columns(4)

c1.metric("Factory Status", st.session_state.status)
c2.metric("Threat Level (%)", threat)
c3.metric("Machine 2", st.session_state.machine2)
c4.metric("Production %", st.session_state.production[-1])

st.divider()

# 🔹 Machines
col1, col2, col3 = st.columns(3)

col1.success("Machine 1: Running")

if st.session_state.machine2 == "Compromised":
    col2.error("Machine 2: COMPROMISED")
else:
    col2.success("Machine 2: Running")

col3.success("Machine 3: Running")

st.divider()

# 🔹 Digital Twin
if st.session_state.twin == "Active":
    st.success("🧬 Digital Twin ACTIVE – Operations Maintained")
else:
    st.info("🧬 Digital Twin Standby")

# 🔹 Production Graph
st.subheader("📈 Production Trend")
st.line_chart(st.session_state.production)

# 🔹 Recovery Time
st.subheader("⏱️ Recovery Performance")

if st.session_state.last_recovery_time:
    st.success(f"{st.session_state.last_recovery_time:.2f} sec")
else:
    st.info("No recovery yet")

# 🔹 Recovery Trend
st.subheader("📊 Recovery Time Trend")

times = st.session_state.recovery_times

if times:
    df = pd.DataFrame({
        "Run": range(1, len(times)+1),
        "Recovery Time": times
    }).set_index("Run")

    st.line_chart(df)
else:
    st.info("No recovery data")
