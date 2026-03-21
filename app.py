# app.py – Teenage Pregnancy Rate Predictor (web interface)

import streamlit as st
import pandas as pd
import joblib

st.set_page_config(page_title="Teenage-PG Predictor", layout="centered")
st.title("Teen Pregnancy Rate Predictor – Bungoma")
st.markdown("Predict **Teen Pregnancy Rate** (%) based on area characteristics")

# Load model & encoders
@st.cache_resource
def load_assets():
    model = joblib.load('teenage-pg-rf-model.pkl')
    encoders = joblib.load('teenage-pg-encoders.pkl')
    return model, encoders

model, encoders = load_assets()

# Dropdown / input options from training
subcounties = encoders['SubCounty'].classes_
wards = encoders['Ward'].classes_

# ── Inputs ──
with st.form("prediction_form"):
    col1, col2 = st.columns(2)
    
    with col1:
        subcounty = st.selectbox("Sub-County", subcounties)
        ward = st.selectbox("Ward", wards)
    
    with col2:
        dropouts = st.number_input("School Dropouts", 0, 500, 40)
        centers = st.number_input("Health Centers", 0, 30, 2)
    
    contra = st.radio("Contraceptive Access", ["Yes", "No"], horizontal=True)
    edu = st.radio("Education Programs", ["Yes", "No"], horizontal=True)
    
    submitted = st.form_submit_button("Predict", type="primary", use_container_width=True)

if submitted:
    # Build input row
    input_df = pd.DataFrame({
        'SubCounty': [subcounty],
        'Ward': [ward],
        'SchoolDropouts': [dropouts],
        'HealthCenters': [centers],
        'ContraceptiveAccess': [contra],
        'EducationPrograms': [edu]
    })
    
    # Encode
    for col, le in encoders.items():
        if col in input_df.columns:
            input_df[col] = le.transform(input_df[col])
    
    # Predict
    pred = model.predict(input_df)[0]
    
    st.success(f"**Predicted Teen Pregnancy Rate: {pred:.2f} %**")
    
    st.markdown("#### Input values used:")
    st.json(input_df.to_dict(orient="records")[0])

st.markdown("---")
st.caption("Local model • Built with Streamlit • Data: bungoma.csv")