import streamlit as st
import pandas as pd
import plotly_express
car_data = pd.read_csv('../vehicles_us.csv') # leer los datos
hist_button = st.button('Construir histograma') # crear un botón
     
if hist_button: # al hacer clic en el botón
         # escribir un mensaje
         st.write('Histograma de venta de coches')
         
         # crear un histograma
         fig = px.histogram(car_data, x="odometer")
     
         # mostrar un gráfico Plotly interactivo
         st.plotly_chart(fig, use_container_width=True)

disp_button = st.button('Contruir Diagrama Dispersión') # crear un botón
     
if hist_button: # al hacer clic en el botón
         # escribir un mensaje
         st.write('Crea un diagrama de dispersión venta de coches')
         
         # crear un histograma
         fig = px.scatter(
            df,
            x="columna_x",
            y="columna_y",
            title="Diagrama de dispersión"
            )

        fig.show()
     
         # mostrar un gráfico Plotly interactivo
st.plotly_chart(fig, use_container_width=True)