
import pandas as pd
import joblib

# Load trained model
model = joblib.load("models/burnout_model.pkl")

print("\n===== STUDENT BURNOUT PREDICTION =====")

# Take student input
study_hours = float(input("Daily Study Hours: "))
sleep_hours = float(input("Daily Sleep Hours: "))
workload = int(input("Workload (1-10): "))
attendance = float(input("Attendance Percentage: "))
breaks = int(input("Daily Breaks: "))
academic_pattern = int(input("Academic Pattern (1-5): "))

# Prepare input data
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

# Predict risk
prediction = model.predict(student_data)[0]

print("\n===== PREDICTION RESULT =====")

if prediction == 1:
    print("⚠️ High Academic Overload Risk")
    print("Suggestion: Take regular breaks and manage your workload.")
else:
    print("✅ Low Academic Overload Risk")
    print("Suggestion: Maintain a balanced study routine.")
