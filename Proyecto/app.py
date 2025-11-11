import streamlit as st
import pandas as pd
import plotly_express as px

car_data = pd.read_csv('vehicles_us.csv')
hist_button = st.button('Construir histograma')  # crear un botón

if hist_button:
    # al hacer clic en el botón escribir un mensaje
    st.write(
        'Creación de un histograma para el conjunto de datos de anuncios de venta de coches')

    # crear un histograma
    fig = px.histogram(car_data, x="odometer")

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)

if scat_button:
    st.write(
        'Creación de un gráfico de dispersión')

    # crear un gráfico de dispersión
    fig_2 = px.scatter(car_data, x="odometer", y="price")
    st.plotly_chart(fig_2, )
