
import streamlit as st
import pandas as pd
import joblib

# Load trained model
model = joblib.load("models/burnout_model.pkl")

st.set_page_config(
    page_title="Student Burnout Early Warning System",
    page_icon="📚",
    layout="wide"
)

st.title("📚 Student Burnout Early Warning System")

st.write(
    "Analyze your academic routine and identify possible academic overload risk."
)

st.sidebar.header("Student Academic Details")

study_hours = st.sidebar.slider(
    "Daily Study Hours", 0.0, 16.0, 6.0
)

sleep_hours = st.sidebar.slider(
    "Daily Sleep Hours", 0.0, 12.0, 7.0
)

workload = st.sidebar.slider(
    "Academic Workload (1-10)", 1, 10, 5
)

attendance = st.sidebar.slider(
    "Attendance Percentage", 0.0, 100.0, 80.0
)

breaks = st.sidebar.slider(
    "Daily Breaks", 0, 10, 3
)

academic_pattern = st.sidebar.slider(
    "Academic Pattern (1-5)", 1, 5, 3
)

# Prepare student data
student_data = pd.DataFrame(
    [[
        study_hours,
        sleep_hours,
        workload,
        attendance,
        breaks,
        academic_pattern
    ]],
    columns=[
        "study_hours",
        "sleep_hours",
        "workload",
        "attendance",
        "breaks",
        "academic_pattern"
    ]
)

st.subheader("Your Academic Routine")

col1, col2, col3 = st.columns(3)

col1.metric("Study Hours", study_hours)
col2.metric("Sleep Hours", sleep_hours)
col3.metric("Workload", workload)

st.dataframe(student_data, use_container_width=True)

if st.button("Analyze Academic Overload Risk"):

    prediction = model.predict(student_data)[0]

    st.subheader("Prediction Result")

    if prediction == 1:
        st.warning("⚠️ High Academic Overload Risk")

        st.write("### Personalized Suggestions")

        if study_hours > 6:
            st.write("- Try shorter study sessions with regular breaks.")

        if sleep_hours < 7:
            st.write("- Make sufficient time for sleep and rest.")

        if workload >= 7:
            st.write("- Divide assignments into smaller manageable tasks.")

        if breaks < 2:
            st.write("- Add regular breaks to your study routine.")

    else:
        st.success("✅ Low Academic Overload Risk")

        st.write("### Suggestions")
        st.write("- Maintain a balanced routine.")
        st.write("- Continue taking regular breaks.")
        st.write("- Keep tracking your academic patterns.")

st.caption(
    "Educational prototype only. This is not a medical diagnosis."
)
