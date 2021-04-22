import numpy as np

def GeometriaDef():
    wezly = np.array([[1,0], [2,1], [3,0.5], [4,0.75]])
    elementy = np.array([[1, 1, 3], [2, 4, 2], [3, 3, 4]])
    wb = [{"ind": 1, "typ":'D',"wartosc":1},{"ind": 2, "typ":'D',"wartosc":2}]
    return wezly,elementy,wb