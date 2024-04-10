#Librerias 
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly_express as px
import plotly.graph_objects as go

#Configurción de página, puede ser "centered" o "wide"

st.set_page_config(page_title="Mi primera APP", layout="wide", page_icon="")
st.set_option('deprecation.showPyplotGlobalUse', False)

#Creación de columna y logotipo 
st.image("img/images.png",width=200)
col1,col2,col3 = st.columns(3)
with col1:
    st.title('Mi primer título')
with col2:
    st.text("Mi primer texto")
    
with col3:
    st.markdown("Mi primer mark")

#Cosas que vamos a usar en todas nuestra app

df0 = pd.read_csv(r"data/netflixprocesado.csv")

if "Unnamed: 0" in df0:
    df0 = df0.drop(columns=["Unnamed: 0"])


def genere_selec(genero_select):
    if genero_select:
        return df0.loc[df0["Tipo"]==genero_select]
    else:
        return ""


#Sidebar con filtros

filtro_pais = st.sidebar.selectbox("País", df0["País"].unique())

if filtro_pais:
    df1 = df0.loc[df0["País"]==filtro_pais]
filtro_genero = st.sidebar.selectbox('Género', df0['Tipo'].unique())

if filtro_genero:
    df1 = df0.loc[df0['Tipo'] == filtro_genero]

#Dibujar dataframe con los filtros

if filtro_pais and filtro_genero:
    df2 = df0.loc[(df0["País"]==filtro_pais)& (df0["Tipo"]==filtro_genero)]

st.dataframe(df2)




#Gráficos
st.title("Mis primeros gráficos")
st.markdown("<center><h2><l style='color:white; font-size: 30px;'>Mis primeros gráficos ( título2 )</h2></center>", unsafe_allow_html=True)
 
col1, col2, col3 = st.columns(3)
with col1:
    top10_paises = df0["País"].value_counts().head(10).to_frame()
    grafica = px.bar(top10_paises, x=top10_paises.index, y="País", template="plotly_dark", width=400, height=400)
    st.plotly_chart(grafica)
 
with col2:
    scatter = px.scatter(df0, "Fecha_de_estreno", "País", title="Gráfica")
    st.plotly_chart(scatter)
 
with col3:
    country_count = df0["País"].value_counts()
    fig = px.pie(country_count.head(10), values="País", names=country_count.head(10).index, title="TOP10")
    st.plotly_chart(fig)