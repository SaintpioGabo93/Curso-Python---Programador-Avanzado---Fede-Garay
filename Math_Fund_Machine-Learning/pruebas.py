import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0, 10, 0.01) #comienza, termina, tamaño de paso
y = np.cos(x)
plt.plot(x, y)
plt.show()