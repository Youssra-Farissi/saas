import scipy
from scipy import spatial

dis_r = spatial.distance.cdist(
    d_list[i]['RS'].values.reshape(-1, len(d_dist[i]['RS'].values))
    ,d_list[i]['RS'].values.reshape(-1, len(d_dist[i]['RS'].values))
)

data_uploader = st.file_uploader("upload file", type=('csv', 'txt', 'las'))
if data_uploader is not None:
    data_uploader.seek(0)
    string = data_uploader.read().decode()

    log=ls.read(string)
    temp_df1=log.df()
    temp_df1=temp_df1.reset_index()
    temp_df1.columns
    temp_df1.rename(columns= {'DEPT: DEPTH'}, inplace = True)
    temp_df1=temp_df1.dropna()

def log_plot(well, df, depth_mdt, depth_mdt_actual, column_depth, column_GR, column_resistivity, column_NPHI, column_RHOB):
    import matplotlib.pyplot as plt
    from matplotlib.ticker import AutoMinorLocator

    fig, ax = plt.subplots(1, 3, figisize=(28, 22), dpi=55)
    fig.subtitle(well[0]+' Well Logs with Highlighted Pressure Recording Points', size=title_size, y=title_height)

    ax[0].minorticks_on()
    ax[0].grid(which='major', linestyle='-', linewidth='1', color='brown')
    ax[0].grid(which='major', linestyle='-', linewidth='1.5', color='black')

    ax[0].minorticks_on()
    ax[0].grid(which='major', linestyle='-', linewidth='1', color='brown')
    ax[0].grid(which='major', linestyle='-', linewidth='1.5', color='black')