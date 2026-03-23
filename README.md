# Teenage Pregnancy Rate Predictor – Bungoma County

![Python](https://img.shields.io/badge/python-3.8%2B-blue?logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-1.20%2B-FF4B4B?logo=streamlit&logoColor=white)
![scikit-learn](https://img.shields.io/badge/scikit--learn-1.0%2B-F7931E?logo=scikitlearn&logoColor=white)
![License](https://img.shields.io/badge/license-MIT-green)

**Interactive web application** that predicts **teen pregnancy rates** (%) in different wards and sub-counties of Bungoma County, Kenya, using a trained **Random Forest** regression model.

Built with **Streamlit** for an easy-to-use interface and trained on local socio-economic and health data.

## ✨ Demo

(You can add a screenshot or GIF here later)

https://github.com/joelwmulongo/teenage-pg/assets/pred.png

## Features

- Predict teen pregnancy rate based on:
  - Sub-County
  - Ward
  - Number of school dropouts
  - Number of health centers
  - Access to contraceptives (Yes/No)
  - Presence of education programs (Yes/No)
- Clean and intuitive Streamlit dashboard
- Model trained with scikit-learn RandomForestRegressor
- Label encoding for categorical variables
- Quick training script included (`train.py`)
