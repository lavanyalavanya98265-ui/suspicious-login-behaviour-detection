# 🔐 Suspicious Login Behaviour Detection

## 📌 Project Overview

Suspicious Login Behaviour Detection is a machine learning based cybersecurity application that identifies whether a login event is **Normal** or **Suspicious**.

The system analyzes behavioural signals from a login event and uses a Logistic Regression model to classify the login.

## 🎯 Problem Statement

Identify login events that exhibit patterns associated with suspicious access.

## 🧠 Machine Learning Approach

The project follows an end-to-end machine learning workflow:

1. Dataset collection
2. Data cleaning and validation
3. Exploratory Data Analysis (EDA)
4. Feature engineering
5. Binary classification
6. Model training and comparison
7. Model evaluation
8. Streamlit application development

## 📊 Input Features

The final model uses five features:

| Feature | Description |
|---|---|
| `login_hour` | Hour at which the login occurred |
| `failed_attempts` | Number of failed login attempts |
| `session_duration` | Duration of the login session in minutes |
| `device_change` | Whether the device changed from the previous login |
| `location_change` | Whether the login location changed from the previous login |

## 🏷️ Target

The original dataset contained multiple login behaviour categories.

They were converted into a binary classification target:

- `0` → Normal
- `1` → Suspicious

## 🤖 Models Evaluated

The following traditional machine learning models were evaluated:

- Logistic Regression
- Decision Tree
- K-Nearest Neighbours (KNN)

The final prototype uses **Logistic Regression**.

## 📈 Model Performance

The final Logistic Regression model achieved:

| Metric | Score |
|---|---:|
| Accuracy | 97% |
| Precision | 48.8% |
| Recall | 62.5% |
| F1-score | 54.8% |
| ROC-AUC | 80.1% |

Because suspicious login events are a minority class, recall, F1-score and ROC-AUC were considered along with accuracy.

## 🔎 Exploratory Data Analysis

EDA was performed to investigate:

- Missing values
- Duplicate records
- Class imbalance
- Feature distributions
- Relationships between login behaviour and suspicious activity
- Feature patterns
- Device and location changes

The dataset contained 5,000 records and had no missing values or duplicate rows.

## 🖥️ Streamlit Application

The project includes a Streamlit application that allows users to enter login details and receive a prediction.

### Application Flow

User Input  
↓  
Feature Processing  
↓  
Logistic Regression Model  
↓  
Normal / Suspicious Prediction  
↓  
Suspicious Probability

## 🛠️ Technologies Used

- Python
- Pandas
- Scikit-learn
- Joblib
- Streamlit
- Jupyter Notebook

## 📁 Project Structure

```text
capstone_final/
│
├── app.py
├── login_detection_model.pkl
├── requirements.txt
├── README.md
└── detectRealOrFake.ipynb