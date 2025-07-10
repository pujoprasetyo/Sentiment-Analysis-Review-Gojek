
import streamlit as st
import eda
import prediction

st.set_page_config(
    page_title='Prediksi Reviews Positif/Negatif',
    initial_sidebar_state='expanded'
)

page = st.sidebar.selectbox('pilih halaman:', ('Prediction', 'EDA'))

if page == 'Prediction':
    prediction.run()
else:
    eda.run()