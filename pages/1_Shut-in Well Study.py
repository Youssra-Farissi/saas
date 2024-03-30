import streamlit as st
import pandas as pd

def main():
    st.title("Téléchargement de données")

    st.write("Veuillez télécharger votre fichier Excel.")

    data_uploader = st.file_uploader("Télécharger fichier Excel (xlsx)", type=["xlsx"])

    if data_uploader is not None:
        st.success("Fichier téléchargé avec succès!")
        data_uploader.seek(0)
        try:
            # Utiliser 'latin-1' pour décoder les données
            string = data_uploader.read().decode("latin-1")
            temp_df1 = pd.read_excel(string)

            # Votre code de traitement des données ici
            # Par exemple:
            temp_df1.rename(columns={'DEPT':'DEPTH','SGRC':'GR','TNPL':'NPHI','PEF':'PE',
                                     'HSI':'CALI','SBD2':'RHOB','PRES2M16IN':'RS','PRES500K48IN':'RT','STOP':'ROP',
                                     'SFXE':'FEXP'}, inplace=True)
            temp_df1 = temp_df1.dropna()
          
            temp_df1 = temp_df1[['DEPTH', 'ROP', 'GR', 'NPHI', 'PE', 'CALI', 'RHOB', 'RS', 'RT', 'ROP', 'FEXP', 'RPM']]
            std_cali = temp_df1['CALI'].std()
            std_gr = temp_df1["GR"].std()
            std_p = temp_df1['NPHI'].mean()
            std_d = temp_df1['RHOB'].mean()
            mean_r = temp_df1['RT'].mean()
            data_df = temp_df1.copy()

        except Exception as e:
            st.error(f"Erreur rencontrée lors du traitement des données: {e}")

if __name__ == "__main__":
    main()
