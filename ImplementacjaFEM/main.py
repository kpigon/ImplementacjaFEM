import numpy as np
import matplotlib.pyplot as plt
import AutomatycznyGeneratorGeometrii as agg
import RysujGeometrie as rg
import GeometriaDefinicja as gd
import Alokacja as al
import FunkcjeBazowe as fb

### PREPROCESSING

#parametry sterujące
c=0
f= lambda x: 0

#geometria

WEZLY, ELEMENTY, WB= gd.GeometriaDef()
n=np.shape(WEZLY)[0]

#x_a=0
#x_b=1
#n=5
#WEZLY,ELEMENTY = agg.generujTabliceGeometrii(x_a,b_a,n)
#WB = [{"ind": 1, "typ":'D',"wartosc":1},{"ind": 2, "typ":'D',"wartosc":2}]


rg.rysujGeometrie(WEZLY,ELEMENTY,WB)

### PROCESSING