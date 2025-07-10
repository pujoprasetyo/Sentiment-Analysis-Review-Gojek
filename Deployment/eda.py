#Library
import streamlit as st
import pandas as pd
import seaborn as sns
import plotly.express as px
import matplotlib.pyplot as plt
from PIL import Image
from wordcloud import WordCloud

def run():
  
  # Load Data
  df = pd.read_csv('./src/clean_data.csv')

  # Title
  st.title('Sentiment Analyst Reviews GOJEK')
  st.markdown('-------')

  # Menambahkan Gambar
  image = Image.open('./src/img1.jpg')
  st.image(image)

  st.subheader('Halaman ini dibuat untuk menampilkan hasil Explatory Data Analysis (EDA) mengenai reviews terhadap aplikasi GOJEK yang ada di Google Play Store')

  # ------------ EDA 1 ------------
  
  st.write('## 1. Perbandingan jumlah data sentiment positif dan negatif')

  # Menghitung jumlah reviews
  label_counts = df['label'].value_counts()
  labels = label_counts.index
  sizes = label_counts.values
  total = sum(sizes)

  # Fungsi untuk menampilkan jumlah dan persentase
  def make_autopct(sizes):
      def my_autopct(pct):
          count = int(round(pct/100.*total))
          return f"{count} ({pct:.1f}%)"
      return my_autopct

  # Plot pie chart
  fig, ax = plt.subplots(figsize=(4, 4))
  plt.pie(sizes,
          labels=labels,
          autopct=make_autopct(sizes),  
          colors=plt.cm.Set3.colors,
          startangle=90)

  st.pyplot(fig)
  st.write('Berdasarkan visualisasi yang ditampilkan jumlah reviews dengan konten positif lebih banyak dari pada konten negatif')
  st.write('Jumlah reviews positif yang ditemukan terdapat sebanyak 4387 reviews dengan persentase 64.3%')
  st.write('Sedangkan reviews negatif yang ditemukan terdapat sebanyak 2437 reviews dengan persentase 35.7%')
  st.markdown('-------')

  # ------------ EDA 2 ------------
  st.write('## 2. Word Cloud Sentiment Negatif')

  # Menggabungkan semua teks negatif jadi satu string
  text = ' '.join(df[df['label'] == 0]['clean_text'].astype(str))

  # Membuat wordcloud dari teks yang dibuat
  wordcloud = WordCloud(width=800, height=400, background_color='white', colormap='Set2').generate(text)

  # Menampilkan data
  fig, ax = plt.subplots(figsize=(10, 5))
  ax.imshow(wordcloud, interpolation='bilinear')
  ax.axis('off') 
  st.pyplot(fig)

  st.write('Wordcloud menampilkan daftar kata-kata yang sering muncul di dalam dataset')
  st.write('Pada sentiment negatif kata-kata yang sering digunakan adalah aplikasi, driver, gojek, dll.')
  st.markdown('-------')

    # ------------ EDA 3 ------------
  st.write('## 3. Word Cloud Sentiment Positif')

  # Menggabungkan semua teks positif jadi satu string
  text2 = ' '.join(df[df['label'] == 1]['clean_text'].astype(str))

  # Membuat wordcloud dari teks yang dibuat
  wordcloud = WordCloud(width=800, height=400, background_color='white', colormap='Set2').generate(text2)

  # Menampilkan data
  fig, ax = plt.subplots(figsize=(10, 5))
  ax.imshow(wordcloud, interpolation='bilinear')
  ax.axis('off') 
  st.pyplot(fig)
  
  st.write('Pada sentiment positif kata-kata yang sering digunakan adalah oke, bagus, bantu, dll.')

if __name__ == '__main__':
  run()