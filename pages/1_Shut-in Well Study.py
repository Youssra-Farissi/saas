import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import AutoMinorLocator

def main():
    st.title("Téléchargement de données")
    st.write("Veuillez télécharger votre fichier Excel.")

    data_uploader = st.file_uploader("Télécharger fichier Excel (xlsx)", type=["xlsx"])

    if data_uploader is not None:
        try:
            st.success("Fichier téléchargé avec succès!")
            data_uploader.seek(0)
            # Read the Excel file using pandas
            temp_df1 = pd.read_excel(data_uploader)
            # Rename columns
            temp_df1.rename(columns={'DEPT':'DEPTH','SGRC':'GR','TNPL':'NPHI','PEF':'PE',
                                     'HSI':'CALI','SBD2':'RHOB','PRES2M16IN':'RS','PRES500K48IN':'RT','STOP':'ROP',
                                     'SFXE':'FEXP'}, inplace=True)
            # Drop rows with missing values
            temp_df1 = temp_df1.dropna()
            # Select desired columns
            temp_df1 = temp_df1[['DEPTH', 'ROP', 'GR', 'NPHI', 'PE', 'CALI', 'RHOB', 'RS', 'RT', 'ROP', 'FEXP', 'RPM']]
            # Calculate standard deviations and means
            std_cali = temp_df1['CALI'].std()
            std_gr = temp_df1['GR'].std()
            std_p = temp_df1['NPHI'].mean()
            std_d = temp_df1['RHOB'].mean()
            mean_r = temp_df1['RT'].mean()
            data_df = temp_df1.copy()
        except Exception as e:
            st.error(f"Erreur rencontrée lors du traitement des données: {e}")

    # Call log_plot function here once all data is loaded and processed
    if 'temp_df1' in locals():  # Check if temp_df1 is defined
        fig1 = log_plot("well_name", temp_df1, "depth_df_mdt", "depth_mdt_actual_708", "DEPTH", "GR", "RT", "NPHI", "RHOB")
        st.text("Données de Hell avec points de collecte HDT mis en évidence")
        st.pyplot(fig1, width=35)

def log_plot(well, df, depth_mdt, depth_mdt_actual, column_depth, column_GR, column_resistivity, column_NPHI, column_RHOB):
    fig, ax = plt.subplots(1, 3, figsize=(28, 22), dpi=55)
    fig.suptitle(f"{well} Well Logs with Highlighted Pressure Recording Points", size=24, y=0.92)

    ax[0].minorticks_on()
    ax[0].grid(which='major', linestyle='-', linewidth=1, color='brown')
    ax[0].grid(which='minor', linestyle=':', linewidth=1.5, color='black')

    ax[1].minorticks_on()
    ax[1].grid(which='major', linestyle='-', linewidth=1, color='brown')
    ax[1].grid(which='minor', linestyle=':', linewidth=1.5, color='black')

    return fig

if __name__ == "__main__":
    main()
