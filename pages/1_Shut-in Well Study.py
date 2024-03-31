import streamlit as st
import pandas as pd
import lasio as ls

def main():
    st.title("Téléchargement de données")

    st.write("Veuillez télécharger votre fichier Excel.")

    data_uploader = st.file_uploader("Télécharger fichier Excel (xlsx)", type=["xlsx"])

    if data_uploader is not None:
        st.success("Fichier téléchargé avec succès!")
        data_uploader.seek(0)
        df = pd.read_excel(data_uploader)
        st.write(df)

if __name__ == "__main__":
    main()
