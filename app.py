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
    if 'audit_completed' not in st.session_state:
        st.session_state.audit_completed = False

    if not st.session_state.audit_completed:
        st.subheader("Audit Form")
        st.write(f"**Advisor:** {st.session_state.advisor_name} | **Auditor:** {st.session_state.auditor_name}")
        st.divider()

        with st.form("audit_form"):
            answers = {}

            for criterion in st.session_state.controller.quality_criteria:
                answer = st.radio(
                    label=criterion.question_text,
                    options=criterion.options,
                    key=f"q_{criterion.id}"
                )
                answers[criterion.id] = answer

            submitted = st.form_submit_button("Calculate Final Score")

            if submitted:
                total_score = 0
                total_possible = 0

                for criterion in st.session_state.controller.quality_criteria:
                    result = criterion.calculate_score(answers[criterion.id])
                    total_score += result["score"]
                    total_possible += result["possible"]
                
                final_percentage = (total_score / total_possible) * 100

                st.session_state.final_percentage = final_percentage
                st.session_state.audit_completed = True
                st.rerun()
    else:
        st.subheader("Results")