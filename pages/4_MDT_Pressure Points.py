import matplotlib.pyplot as plt
from matplotlib.ticker import AutoMinorLocator

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

fig1 = log_plot(well_name, temp_df1, depth_df_mdt, depth_mdt_actual_708, "DEPTH", "GR", "RT", "NPHI", "RHOB")

st.text("Hell Data with Highlighted HDT Points")
st.pyplot(fig1, width=35)
