import streamlit as st
import scipy
from scipy import spatial
import pandas as pd

data1 = {'RS': [1, 2, 3, 4], 'RT': [5, 6, 7, 8]}
data2 = {'RS': [9, 10, 11, 12], 'RT': [13, 14, 15, 16]}

df1 = pd.DataFrame(data1)
df2 = pd.DataFrame(data2)

d_list = [df1, df2] 

dis_r_list = []
for df in d_list:
    dis_r = spatial.distance.cdist(
        df['RS'].values.reshape(-1, len(df['RS'].values)),
        df['RT'].values.reshape(-1, len(df['RT'].values))
    )
    dis_r_list.append(dis_r)

# Afficher les résultats sur la page
st.title("Distances entre les colonnes RS et RT")
for i, dis_r in enumerate(dis_r_list):
    st.write(f"DataFrame {i+1}:")
    st.dataframe(dis_r)
