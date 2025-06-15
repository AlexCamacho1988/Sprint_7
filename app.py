import pandas as pd
import plotly.express as px
import streamlit as st

st.header('Data viewer')

car_data = pd.read_csv('vehicles_us.csv')  # leer los datos
# hist_button = st.button('Construir histograma')  # crear un botón
# scatter_button = st.button('Construir dispersion')  # crear un botón
build_histogram = st.checkbox('Construir un histograma')  # crear casilla
build_scatter = st.checkbox('Construir dispersión')  # crear casilla

if build_histogram:  # al hacer clic en el botón
    # escribir un mensaje
    st.write(
        'Creación de un histograma para el conjunto de datos de anuncios de venta de coches')

    # crear un histograma
    fig = px.histogram(car_data, x="odometer")

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)

if build_scatter:  # al hacer clic en el botón
    # escribir un mensaje
    st.write('Creación de gráfico de dispersión para el conjunto de datos de anuncios de venta de coches')

    # crear un histograma
    fig2 = px.scatter(car_data, x="odometer", y='price')

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig2, use_container_width=True)
