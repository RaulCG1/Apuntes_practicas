import numpy as np
import matplotlib.pyplot as ply
"""
arreglo = np.array([1,2,3,4,5])
print(arreglo)
print(arreglo[2])
print(arreglo.sum())"""

x = np.linspace(0,np.pi,num=100)
y = np.sin(x)

ply.plot(x,y)
