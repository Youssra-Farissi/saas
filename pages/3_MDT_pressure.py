import scipy
from scipy import spatial
import pandas as pd

data1 = {'RS': [1, 2, 3, 4], 'RT': [5, 6, 7, 8]}
data2 = {'RS': [9, 10, 11, 12], 'RT': [13, 14, 15, 16]}

df1 = pd.DataFrame(data1)
df2 = pd.DataFrame(data2)

d_list = [df1, df2] 
dis_r = spatial.distance.cdist(
      d_list[i]['RS'].values.reshape(-1, len(d_list[i]['RS'].values)),
      d_list[i]['RT'].values.reshape(-1, len(d_list[i]['RT'].values))
)
