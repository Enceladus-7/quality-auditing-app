import streamlit as st
from logic import QualityController

st.set_page_config(page_title="Quality Auditing App",layout="centered")

if 'controller' not in st.session_state:
    st.session_state.controller = QualityController()
    st.session_state.controller.load_criteria_from_csv('criteria.csv')

if 'audit_started' not in st.session_state:
    st.session_state.audit_started = False

st.title("Quality Auditing App")

if not st.session_state.audit_started:
    st.subheader("Setup")
    advisor_name = st.text_input("Advisor:")
    auditor_name = st.text_input("Auditor:")

    if st.button("Start"):
        if advisor_name and auditor_name:
            st.session_state.advisor_name = advisor_name
            st.session_state.auditor_name = auditor_name
            st.session_state.audit_started = True
            st.rerun()
        else:
            st.warning("Please enter both names to begin.")

else:
    st.success(f"Audit started for Advisor: {st.session_state.advisor_name}")