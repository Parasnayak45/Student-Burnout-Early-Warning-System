# Student Burnout Early Warning System

An AI-Based Student Burnout Prediction and Early Warning System designed to identify academic overload risks using students' academic and lifestyle patterns.

## Project Overview

The Student Burnout Early Warning System is a machine learning-based project that analyzes student-related information such as:

- Daily Study Hours
- Daily Sleep Hours
- Academic Workload
- Attendance Percentage
- Daily Breaks
- Academic Patterns

The system predicts academic overload risk and provides suggestions to help students maintain a balanced study routine.

## Project Objectives

- Identify potential academic overload risks.
- Analyze student academic and lifestyle patterns.
- Predict burnout risk using Machine Learning.
- Provide helpful study routine suggestions.
- Display predictions through an interactive dashboard.

## Technologies Used

- Python
- Streamlit
- Pandas
- NumPy
- Scikit-learn
- Joblib
- Machine Learning

## Machine Learning Model

**Random Forest Classifier**

The project uses a trained machine learning model to analyze student-related input features and predict academic overload risk.

Model file: `models/burnout_model.pkl`

## Project Structure

```text
Student-Burnout-Early-Warning-System/
│
├── app_folder/
│   ├── app.py
│   └── app_backup.py
│
├── dataset/
│   └── student_data.csv
│
├── models/
│   └── burnout_model.pkl
│
├── src/
│   ├── app.py
│   ├── data_analysis.py
│   ├── generate_dataset.py
│   ├── predict.py
│   └── train_model.py
│
├── .gitignore
└── README.md
```

## How It Works

1. Student enters academic and lifestyle information.
2. The system processes the input data.
3. The trained Machine Learning model analyzes the information.
4. The system predicts academic overload risk.
5. The dashboard displays the prediction and helpful suggestions.

## Installation

Install the required Python libraries:

```bash
pip install streamlit pandas numpy scikit-learn joblib
```

## Run the Project

Run the Streamlit application using the verified dashboard file.

For example, if your working dashboard is `src/app.py`:

```bash
streamlit run src/app.py
```

If your working dashboard is `app_folder/app.py`, use:

```bash
streamlit run app_folder/app.py
```

## Future Scope

- Improve prediction accuracy.
- Add more student-related features.
- Develop personalized recommendations.
- Add student performance analytics.
- Improve dashboard visualization.

## Project Information

**Project Name:** Student Burnout Early Warning System

**Domain:** Artificial Intelligence and Machine Learning

**Technology:** Python, Machine Learning and Streamlit

**GitHub Repository:**  
https://github.com/Parasnayak45/Student-Burnout-Early-Warning-System

---

*This project is developed for academic purposes to support student academic well-being through Machine Learning.*