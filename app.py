import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression

#importando o dataset
df = pd.read_csv(r"C:\Users\ffran\workspace\prevendo valor da pizza com machine learning\pizzas.csv")

#importando o modelo de machine learing
modelo = LinearRegression()
x = df[["diametro"]]
y = df[["preco"]]

#treinando o modelo
modelo.fit(x,y)
st.title("Prevendo valor de uma pizza")
st.divider()

#definindo uma variavel para ter as respostas
diametro = st.number_input("digite o tamanho do diametro da pizza:")

#limitando a resposta à apenas números
if diametro:
    preco_previsto = modelo.predict([[diametro]])[0][0]
    st.write(f"O valor da pizza com o diametro de {diametro:.2f} é de de R${preco_previsto:.2f}")
    st.balloons()