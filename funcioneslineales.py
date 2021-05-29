import matplotlib.pyplot as plt   # librería para graficar
import numpy as np                # librería para manejo de vectores y utilidades matemáticas

N = 100 # número de puntos

def f(m,x,b):
  return m*x + b


m = (7-6)/(3-2)

x = np.linspace(-10.0, 10.0, num=N)

b = 10

y = f(m,x,b)


fig, ax = plt.subplots()
ax.plot(x, y)
ax.grid()
ax.axhline(y=0, color='r')
ax.axvline(x=0, color='r')
plt.show()