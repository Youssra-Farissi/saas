import streamlit as st

def main():
    st.title("Téléchargement de données")

    st.write("Veuillez télécharger votre fichier Excel.")

    # Utilisez st.file_uploader avec le paramètre `type` pour spécifier les extensions autorisées
    data_uploader = st.file_uploader("Télécharger fichier Excel (xlsx)", type=["xlsx"])

    if data_uploader is not None:
        # Vérifiez si un fichier a été téléchargé
        st.success("Fichier téléchargé avec succès!")
        # Réinitialisez le tampon pour vous assurer que le fichier peut être lu correctement
        data_uploader.seek(0)
        # Utilisez le contenu du fichier pour effectuer des opérations supplémentaires
        # Par exemple, vous pouvez utiliser la bibliothèque pandas pour lire le fichier Excel
        # Exemple : 
        # df = pd.read_excel(data_uploader)
        # st.write(df)

if __name__ == "__main__":
    main()
