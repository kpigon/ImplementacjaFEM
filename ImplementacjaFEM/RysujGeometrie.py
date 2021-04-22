import numpy as np
import matplotlib.pyplot as plt

def rysujGeometrie(wezly,elementy,wb):
    il_wezlow=len(wezly)
    y=np.zeros((il_wezlow,1))
    plt.plot(wezly[:,1],y,'r.')
    plt.show()