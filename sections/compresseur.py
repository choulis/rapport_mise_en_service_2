import streamlit as st
from pandas import DataFrame

def afficher_section():
    st.title("Compresseurs")
    nb_compresseur = st.text_input('La centrale contient combien de compresseurs?')

    try:
        dict_compresseurs = {
            f"CP{nb}" : ["", "", "", "", "", "", "", "", ""] for nb in range(1, int(nb_compresseur) + 1)
        }
        tableau_compresseurs = DataFrame(
            {
                "" : ["Information", "Fabricant" , "Modele", "N de serie", "Tension (V)", "Frequence (Hz)", "couplage (delta ou Y)", "Instensite plaque (A)", "Intensite regle en GV (A)"],
                **dict_compresseurs
            }
        )

        tableau_compresseurs = st.data_editor(tableau_compresseurs)
        return tableau_compresseurs
    except:
        st.info("Definir le nombre de compresseurs")
