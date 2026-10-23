import streamlit as st
from calculs import addition

st.title("Calculatrice")

a = st.number_input("Premier nombre", value=0.0)
b = st.number_input("Deuxième nombre", value=0.0)

operation = st.selectbox("Opération", ["Addition"])

if st.button("Calculer"):
    if operation == "Addition":
        result = addition(a, b)
        st.write(f"Résultat: {result}")
