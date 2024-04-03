import pandas as pd
import plotly.express as px
import streamlit as st

st.header('HISTOGRAMA AUTOS')

car_data = pd.read_csv('notebooks/vehicles_us.csv') # leer los datos

build_histogram = st.checkbox('Construir un histograma')

if build_histogram: # si la casilla de verificación está seleccionada
    # escribir un mensaje
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
    
    # crear un histogram
    fig = px.scatter(car_data, x="odometer", y="price")
    
    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)