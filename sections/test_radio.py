import streamlit as st


def afficher_section():
    choix = st.radio("Cochez moi", ['un', 'deux', 'trois'])
    return choix