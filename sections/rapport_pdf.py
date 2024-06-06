import streamlit as st
from datetime import datetime
import pdfkit
from rapport.modele import generer_html

config = pdfkit.configuration(wkhtmltopdf="wkhtmltopdf.exe")

def afficher_section(tableau_compresseur, choix, test_compresseur, test_pressostat):
    st.title("Generer le rapport")
    generer = st.button("Generer")

    if generer:
        html = generer_html(
            title="Rapport des compresseurs",
            tableau= tableau_compresseur,
            choix= choix,
            test_compresseur = "Test compresseur effectue" if test_compresseur else 'Test compresseur non effectue',
            test_pressostat= "Test pressostat effectue" if test_pressostat else 'Test pressostat non effectue'
            )
        aujourdhui = datetime.today()
        nom_fichier = f"Rapport_mise_en_service_compresseurs_{aujourdhui.day}-{aujourdhui.month}-{aujourdhui.year}.pdf"

        pdfkit.from_string(html, nom_fichier)

        with open(nom_fichier, 'rb') as pdf_file:
            pdf_bytes = pdf_file.read()

        st.download_button("Telecharger le rapport", pdf_bytes, nom_fichier)