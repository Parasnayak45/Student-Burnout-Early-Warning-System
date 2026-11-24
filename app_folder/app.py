
import streamlit as st
import pandas as pd
import joblib
from pathlib import Path

# -------------------------------
# PAGE CONFIGURATION
# -------------------------------

st.set_page_config(
    page_title="Student Burnout Early Warning System",
    page_icon="📚",
    layout="wide"
)

# -------------------------------
# LOAD MODEL
# -------------------------------

BASE_DIR = Path(__file__).resolve().parent.parent

MODEL_PATH = BASE_DIR / "models" / "burnout_model.pkl"

model = joblib.load(MODEL_PATH)

# -------------------------------
# CUSTOM DESIGN
# -------------------------------

st.markdown("""
<style>

.stApp {
    background-color: #f4f7fb;
}

.main-title {
    font-size: 36px;
    font-weight: bold;
    color: #243b64;
}

.subtitle {
    font-size: 17px;
    color: #64748b;
}

div[data-testid="stMetric"] {
    background-color: white;
    padding: 20px;
    border-radius: 12px;
    border: 1px solid #e2e8f0;
}

div.stButton > button {
    background-color: #3457d5;
    color: white;
    border-radius: 10px;
    height: 50px;
    width: 100%;
    font-size: 17px;
    font-weight: bold;
}

div.stButton > button:hover {
    background-color: #243b9b;
    color: white;
}

</style>
""", unsafe_allow_html=True)

# -------------------------------
# MAIN TITLE
# -------------------------------

st.markdown(
    '<p class="main-title">📚 Student Burnout Early Warning System</p>',
    unsafe_allow_html=True
)

st.markdown(
    '<p class="subtitle">Analyze academic routines and identify possible academic overload risk.</p>',
    unsafe_allow_html=True
)

st.divider()

# -------------------------------
# SIDEBAR INPUTS
# -------------------------------

st.sidebar.title("🎓 Student Details")
st.sidebar.write("Enter your academic routine.")

study_hours = st.sidebar.slider(
    "Daily Study Hours",
    0.0, 16.0, 6.0, 0.5
)

sleep_hours = st.sidebar.slider(
    "Daily Sleep Hours",
    0.0, 12.0, 7.0, 0.5
)

workload = st.sidebar.slider(
    "Academic Workload (1-10)",
    1, 10, 5
)

attendance = st.sidebar.slider(
    "Attendance Percentage",
    0.0, 100.0, 80.0
)

breaks = st.sidebar.slider(
    "Daily Breaks",
    0, 10, 3
)

academic_pattern = st.sidebar.slider(
    "Academic Pattern (1-5)",
    1, 5, 3
)

# -------------------------------
# STUDENT DATA
# -------------------------------

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

# -------------------------------
# DASHBOARD METRICS
# -------------------------------

st.subheader("📊 Academic Overview")

col1, col2, col3 = st.columns(3)

col1.metric("📖 Study Hours", f"{study_hours} hrs")
col2.metric("😴 Sleep Hours", f"{sleep_hours} hrs")
col3.metric("📝 Workload", f"{workload}/10")

col4, col5, col6 = st.columns(3)

col4.metric("📅 Attendance", f"{attendance}%")
col5.metric("☕ Daily Breaks", breaks)
col6.metric("📈 Academic Pattern", f"{academic_pattern}/5")

st.divider()

# -------------------------------
# STUDENT DATA TABLE
# -------------------------------

st.subheader("📋 Student Academic Data")

st.dataframe(
    student_data,
    use_container_width=True,
    hide_index=True
)

# -------------------------------
# PREDICTION
# -------------------------------

st.subheader("🔍 Academic Overload Analysis")

if st.button("Analyze Academic Overload Risk"):

    prediction = model.predict(student_data)[0]

    st.subheader("Prediction Result")

    if prediction == 1:

        st.warning("⚠️ High Academic Overload Risk")

        st.write("### 💡 Personalized Suggestions")

        if study_hours > 6:
            st.write(
                "- Divide study time into manageable sessions."
            )

        if sleep_hours < 7:
            st.write(
                "- Try to maintain a regular sleep and rest routine."
            )

        if workload >= 7:
            st.write(
                "- Divide assignments into smaller tasks."
            )

        if breaks < 2:
            st.write(
                "- Include regular breaks in your study routine."
            )

        if (
            study_hours <= 6
            and sleep_hours >= 7
            and workload < 7
            and breaks >= 2
        ):
            st.write(
                "- Review your academic schedule and seek support if needed."
            )

    else:

        st.success("✅ Low Academic Overload Risk")

        st.write("### 💡 Suggestions")

        st.write(
            "- Maintain a balanced academic routine."
        )

        st.write(
            "- Continue taking regular breaks."
        )

        st.write(
            "- Keep tracking your academic patterns."
        )

# -------------------------------
# FOOTER
# -------------------------------

st.divider()

st.caption(
    "Student Burnout Early Warning System | "
    "Educational prototype only — not a medical diagnosis."
)
