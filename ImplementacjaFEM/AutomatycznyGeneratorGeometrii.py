import numpy as np

def generujTabliceGeometrii(x_0, x_p, n):
    temp = np.arange(1,n+1)
    WEZLY = (np.vstack((temp.T,x.T)).T)
    temp = np.arange(1,n)
    C1=np.arange(1,n)
    C2=np.arange(2,n+1)
    ELEMENTY = (np.block([[temp],[C1],[C2]])).T
    return WEZLY, ELEMENTY