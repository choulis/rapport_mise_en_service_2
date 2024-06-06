import streamlit as st


def afficher_section():
    st.title("Lancement des tests")
    test_compresseur = st.checkbox("Test sur les compresseurs")
    test_pressostat = st.checkbox("Test pressostat")
    return test_compresseur, test_pressostat