# Import library
import streamlit as st
import pickle
import pandas as pd
import numpy as np
from PIL import Image
from tensorflow.keras.models import load_model
import tensorflow_hub as hub

# Load model
model = load_model('./src/model_nlp', custom_objects={'KerasLayer': hub.KerasLayer})

def run():
    # Title
    st.title('Aplikasi Prediksi Review Bersentimen Positif atau Negatif')

     # Menambahkan Gambar
    image = Image.open('./src/img2.png')
    st.image(image)

    # Sub Header
    st.subheader('Halaman ini berisi aplikasi untuk memprediksi apakah sebuah review memiliki sentimen negatif atau positif')

    # Membuat header form
    st.markdown("<h3 style='text-align:center;'>Silahkan Masukkan Kalimat Reviews pada Form Dibawah</h3>", unsafe_allow_html=True)

    # Membuat form
    with st.form(key='sentiment'):

        teks = st.text_input('Teks Review', placeholder='--masukkan kalimat yang diinginkan--', help='Masukkan kalimat')
        
        st.markdown('----')

        
        submitted = st.form_submit_button('Predict')

        data_inf= pd.DataFrame([teks])

        if submitted:
            
            # Model
            pred_inf = model.predict(data_inf[0])
            # Mengubah data biner
            result = np.where(pred_inf >= 0.5, 1, 0)

            if result <1:
                st.write(f'Teks yang anda masukkan :')
                st.write(data_inf.iloc[0,0])
                st.write('Prediksi: ')
                st.error(f"### Kalimat bersentiment negatif")
                st.markdown('----')
            else:
                st.write(f'Teks yang anda masukkan : ')
                st.write(data_inf.iloc[0,0])
                st.write('Prediksi: ')
                st.success(f"### Kalimat bersentiment positif")
                st.markdown('----')

if __name__ == '__main__':
  run()