import numpy as np
import matplotlib.pyplot as plt

#parametry sterujące
c=0
f=0

#geometria
x_a=0
x_b=1
wezly = np.array([[1,0], [2,1], [3,0.5], [4,0.75]])
elementy = np.array([[1, 1, 3], [2, 4, 2], [3, 3, 4]])

twb_L = 'D'
twb_P = 'D'
wwb_L = 0
wwb_P = 1

def generujTabliceGeometrii(x_0, x_p, n):
    temp = (x_p - x_0) / (n - 1)
    matrix = np.array([x_0])

    for i in range(1, n, 1):
        matrix = np.block([matrix, i * temp + x_0])
    return matrix

def rysujGeometrie(wezly,elementy):
    il_wezlow=wezly.size()
    y=np.zeros((il_wezlow,1))
    plt.plot(wezly[:,1],y,'r.')

print(generujTabliceGeometrii(1,2,5))