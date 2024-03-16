import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Carga de datos
@st.cache_data
def load_data():
    data = pd.read_csv("train.csv")
    return data

# Título de la aplicación
st.title("Análisis de Datos del Titanic")

# Carga de datos
data = load_data()

# Mostrar datos
st.header("Datos")
st.write(data.head())

# Mostrar estadísticas descriptivas
st.header("Estadísticas Descriptivas")
st.write(data.describe())

# Visualización de la distribución de edades
st.header("Distribución de Edades")
fig, ax = plt.subplots()
sns.histplot(data=data, x="Age", ax=ax)
st.pyplot(fig)

# Visualización de la tasa de supervivencia por clase
st.header("Tasa de Supervivencia por Clase")
fig, ax = plt.subplots()
sns.barplot(x="Pclass", y="Survived", data=data, ax=ax)
ax.set_xlabel("Clase")
ax.set_ylabel("Tasa de Supervivencia")
st.pyplot(fig)

# Filtro de datos
st.header("Filtro de Datos")
selected_class = st.selectbox("Selecciona una Clase", options=data["Pclass"].unique())
filtered_data = data[data["Pclass"] == selected_class]
st.write(filtered_data)