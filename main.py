import streamlit as st

from sections import compresseur

st.set_page_config(
    page_title= "Rapport de mise en service",
    layout= 'centered'
)

st.title('Rapport de mise en service')

compresseur.afficher_compresseur_section()