# -*- coding: utf-8 -*-
"""codigoBase.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1q2WqxaQZMmGLPKRpRFEwCrRR63YxftXp
"""

import pandas as pd
import plotly.express as px
import streamlit as st

#Lendo o dataset
df = pd.read_csv('https://raw.githubusercontent.com/wcota/covid19br/master/cases-brazil-states.csv')

#Mellhorando o nome das colunas da tabela
df = df.rename(columns={'newDeaths': 'Novos óbitos', 'newCases': 'Novos casos', 'deaths_per_100k_inhabitants': 'Óbitos por 100mil habitantes', 'totalCases_per_100k_inhabitants': 'Casos por 100mil habitantes'})

#Seleção de Estados
estados = list(df['state'].unique())
state = st.sidebar.selectbox('Qual Estado?', estados)

#Seleção da Coluna
#column = 'Casos por 100mil habitantes'
colunas = ['Novos óbitos', 'Novos casos', 'Óbitos por 100mil habitantes', 'Casos por 100mil habitantes']
column = st.sidebar.selectbox('Qual tipo de informação?', colunas)

#Seleçõ das linhas que pertencem ao Estado
df= df[df['state'] == state]

fig = px.line(df, x='date', y= column, title = column + '-'+ state)
fig.update_layout( xaxis_title = 'Data', yaxis_title =column.upper(), title = {'x': 0.5} )

st.title('DADOS COVID - BRASIL')
st.write('Nessa aplicação, o usuário tem a opção de escolher o estado e o tipo de informação para mostrar o gráfico. Utilize o menu lateral para alterar a mostragem')

st.plotly_chart(fig, use_container_width=True)

st.caption('Os dados foram obtidos a partir do site : https://github.com/wcota/covid19br.git')