
import pandas as pd
import numpy as np
from pathlib import Path

# Project folder location
BASE_DIR = Path(__file__).resolve().parent.parent

# Dataset file location
DATASET_PATH = BASE_DIR / "dataset" / "student_data.csv"

# Load existing dataset
old_data = pd.read_csv(DATASET_PATH)

# Random generator
rng = np.random.default_rng(42)

# Generate additional student records
new_records = []

for i in range(480):

    study_hours = rng.uniform(2, 10)
    sleep_hours = rng.uniform(4, 9)
    workload = rng.integers(1, 11)
    attendance = rng.integers(50, 101)
    breaks = rng.integers(1, 6)
    academic_pattern = rng.integers(1, 6)

    # Academic overload score
    score = (
        study_hours * 0.20
        + workload * 0.40
        + (8 - sleep_hours) * 0.25
        + (100 - attendance) * 0.03
        - breaks * 0.15
    )

    # Add some randomness
    score += rng.normal(0, 0.6)

    # Assign overload risk
    overload_risk = 1 if score > 5.0 else 0

    new_records.append({
        "study_hours": round(study_hours, 1),
        "sleep_hours": round(sleep_hours, 1),
        "workload": workload,
        "attendance": attendance,
        "breaks": breaks,
        "academic_pattern": academic_pattern,
        "overload_risk": overload_risk
    })

# Convert generated records into DataFrame
new_data = pd.DataFrame(new_records)

# Combine old and new data
combined_data = pd.concat(
    [old_data, new_data],
    ignore_index=True
)

# Save updated dataset
combined_data.to_csv(DATASET_PATH, index=False)

print("DATASET GENERATED SUCCESSFULLY!")
print("Total Records:", len(combined_data))
print("\nDataset Preview:")
print(combined_data.head())

print("\nOverload Risk Distribution:")
print(combined_data["overload_risk"].value_counts())
