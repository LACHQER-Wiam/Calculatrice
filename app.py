import streamlit as st
from calculs import addition, soustraction, multiplication, division

st.title("Calculatrice")

a = st.number_input("Premier nombre", value=0.0)
b = st.number_input("Deuxième nombre", value=0.0)

operation = st.selectbox("Opération", ["Addition", "Soustraction", "Multiplication", "Division"])

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
    elif operation == "Division":
        try:
            result = division(a, b)
            st.write(f"Résultat: {result}")
        except ValueError as e:
            st.error(str(e))