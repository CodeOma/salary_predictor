import streamlit as st

from predict_page import show_predict_page
from data_page import show_data_page


page = st.sidebar.selectbox("Data VisualizationOr Predict", ("Predict", "Data Visualization"))

if page == "Predict":
    show_predict_page()
else:
    show_data_page()
