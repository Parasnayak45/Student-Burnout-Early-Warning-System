
import pandas as pd

# Load dataset
data = pd.read_csv("dataset/student_data.csv")

# Display first 5 rows
print("\nSTUDENT BURNOUT DATASET")
print(data.head())

# Display dataset information
print("\nDATASET INFORMATION")
print(data.info())

# Check missing values
print("\nMISSING VALUES")
print(data.isnull().sum())

# Display basic statistics
print("\nDATASET STATISTICS")
print(data.describe())
