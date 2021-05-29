
import matplotlib.pyplot as plt   # librería para graficar
import numpy as np                # librería para manejo de vectores y utilidades matemáticas

N = 100 # número de puntos
def f(x):
  return 2*x**7 - x**4 + 3*x**2 + 4

x = np.linspace(-100.0, 100.0, num=N)

y = f(x)

fig, ax = plt.subplots()
ax.plot(x, y)
ax.grid()
ax.axhline(y=0, color='r')
ax.axvline(x=0, color='r')
plt.show()