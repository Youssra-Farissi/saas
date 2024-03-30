import streamlit as st

def main():
    st.title("Téléchargement de données")

    st.write("Veuillez télécharger votre fichier Excel.")

    # Utilisez st.file_uploader avec le paramètre `type` pour spécifier les extensions autorisées
    data_uploader = st.file_uploader("Télécharger fichier Excel (xlsx)", type=["xlsx"])

    if data_uploader is not None:
        # Vérifiez si un fichier a été téléchargé
        st.success("Fichier téléchargé avec succès!")
        data_uploader.seek(0)
        string = data_uploader.read().decode()

        log=ls.read(string)
        temp_df1=log.df()
        temp_df1=temp_df1.reset_index()
        temp_df1.columns
        temp_df1.rename(columns={'DEPT':'DEPTH','SGRC':'GR','TNPL':'NPHI','PEF':'PE','HSI':'CALI','SBD2':'RHOB','PRES2M16IN':'RS','PRES500K48IN':'RT','STOP':'ROP',
        'SFXE':'FEXP'},inplace=true)
        temp_df1=temp_df1.dropna()
       
if __name__ == "__main__":
    main()
