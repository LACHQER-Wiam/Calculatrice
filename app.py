import streamlit as st
from calculs import addition, soustraction, multiplication

st.title("Calculatrice")

a = st.number_input("Premier nombre", value=0.0)
b = st.number_input("Deuxième nombre", value=0.0)

operation = st.radio("Choisissez une opération", ("Addition", "Soustraction", "Multiplication"))

if st.button("Calculer"):
    if operation == "Addition":
        result = addition(a, b)
        st.write(f"Résultat: {result}")
    elif operation == "Soustraction":
        result = soustraction(a, b)
        st.write(f"Résultat: {result}")
    elif operation == "Multiplication":
        result = multiplication(a, b)
        st.write(f"Résultat: {result}")
