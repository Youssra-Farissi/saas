import streamlit as st
import pandas as pd
import lasio as ls

def main():
    st.title("Téléchargement de données")

    st.write("Veuillez télécharger votre fichier Excel.")

    # Utilisez st.file_uploader avec le paramètre `type` pour spécifier les extensions autorisées
    data_uploader = st.file_uploader("Télécharger fichier Excel (xlsx)", type=["xlsx"])

    if data_uploader is not None:
        # Vérifiez si un fichier a été téléchargé
        st.success("Fichier téléchargé avec succès!")
        data_uploader.seek(0)
        # Lecture du contenu du fichier Excel en tant que DataFrame pandas
        df = pd.read_excel(data_uploader)
        # Afficher le DataFrame pandas
        st.write(df)

if __name__ == "__main__":
    main()
