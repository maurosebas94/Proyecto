import streamlit as st
import pandas as pd
import plotly.express as px
car_data = pd.read_csv('vehicles_us.csv') # leer los datos
hist_button = st.button('Construir histograma') # crear un botón
     
if hist_button: # al hacer clic en el botón
   fig = px.histogram(car_data, x="odometer") # crear un histograma
   fig.show() # crear gráfico de dispersión

disp_button = st.button('Construir diagrama dispersion') # crear un botón
if disp_button: # al hacer clic en el botón
   fig = px.scatter(car_data, x="odometer", y="price") # crear un gráfico de dispersión
   fig.show() # crear gráfico de dispersión