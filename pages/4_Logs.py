import streamlit as st

st.title("📜 System Logs")

logs = st.session_state.get("logs", [])

if logs:
    for log in logs[::-1]:
        st.write(log)
else:
    st.write("No logs yet")
