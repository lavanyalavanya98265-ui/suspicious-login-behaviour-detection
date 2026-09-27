import streamlit as st
import joblib
import pandas as pd

# -----------------------------
# Load trained model
# -----------------------------
model = joblib.load("login_detection_model.pkl")

# -----------------------------
# Page configuration
# -----------------------------
st.set_page_config(
    page_title="Suspicious Login Detection",
    page_icon="🔐",
    layout="centered"
)

# -----------------------------
# Title
# -----------------------------
st.title("🔐 Suspicious Login Behaviour Detection")

st.write(
    "Detect whether a login event appears normal or suspicious "
    "using machine learning."
)

st.divider()

# -----------------------------
# Model Information
# -----------------------------
with st.expander("📊 Model Information"):
    st.write("**Algorithm:** Logistic Regression")
    st.write("**Input Features:** 5")
    st.write("**Accuracy:** 97%")
    st.write("**Recall:** 62.5%")
    st.write("**F1-score:** 54.8%")
    st.write("**ROC-AUC:** 80.1%")

st.divider()

# -----------------------------
# Login Inputs
# -----------------------------
st.subheader("Enter Login Details")

login_hour = st.slider(
    "🕐 Login Hour",
    min_value=0,
    max_value=23,
    value=12
)

failed_attempts = st.number_input(
    "❌ Failed Attempts",
    min_value=0,
    max_value=50,
    value=0,
    step=1
)

session_duration = st.number_input(
    "⏱️ Session Duration (minutes)",
    min_value=0.0,
    max_value=120.0,
    value=30.0,
    step=1.0
)

device_change = st.selectbox(
    "💻 Device Changed?",
    ["No", "Yes"]
)

location_change = st.selectbox(
    "📍 Location Changed?",
    ["No", "Yes"]
)

# Convert Yes/No to 0/1
device_change_value = 1 if device_change == "Yes" else 0
location_change_value = 1 if location_change == "Yes" else 0

st.divider()

# -----------------------------
# Prediction
# -----------------------------
if st.button("🔍 Check Login", use_container_width=True):

    input_data = pd.DataFrame([[
        login_hour,
        failed_attempts,
        session_duration,
        device_change_value,
        location_change_value
    ]], columns=[
        "login_hour",
        "failed_attempts",
        "session_duration",
        "device_change",
        "location_change"
    ])

    prediction = model.predict(input_data)[0]
    probability = model.predict_proba(input_data)[0][1]

    st.subheader("Prediction Result")

    if prediction == 1:
        st.error("🚨 SUSPICIOUS LOGIN")
    else:
        st.success("✅ NORMAL LOGIN")

    st.metric(
        "Suspicious Probability",
        f"{probability:.2%}"
    )

    st.progress(float(probability))

st.divider()

st.caption(
    "ML-based educational prototype for suspicious login behaviour detection."
)