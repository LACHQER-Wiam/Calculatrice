import streamlit as st
from calculs import addition, soustraction

st.title("Calculatrice")

a = st.number_input("Premier nombre", value=0.0)
b = st.number_input("Deuxième nombre", value=0.0)

operation = st.selectbox("Opération", ["Addition", "Soustraction"])

if st.button("Calculer"):
    if operation == "Addition":
        result = addition(a, b)
        st.write(f"Résultat: {result}")
    elif operation == "Soustraction":
        result = soustraction(a, b)
        st.write(f"Résultat: {result}")
