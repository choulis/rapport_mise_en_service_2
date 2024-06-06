import streamlit as st

from sections import compresseur, rapport_pdf, test_radio, test_checkboxes

st.set_page_config(
    page_title= "Rapport de mise en service",
    layout= 'centered'
)

st.title('Rapport de mise en service')

tableau_compresseur = compresseur.afficher_section()
choix = test_radio.afficher_section()
test_compresseur, test_pressostat = test_checkboxes.afficher_section()

if tableau_compresseur is not None:
    rapport_pdf.afficher_section(tableau_compresseur, choix, test_compresseur, test_pressostat)
    