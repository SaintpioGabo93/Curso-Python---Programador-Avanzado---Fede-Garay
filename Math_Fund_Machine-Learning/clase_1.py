#Esta es la libreria en para matemáticas
import numpy as np
import matplotlib.pyplot as plt
#Se declara la variable del tiempo
tiempo = np.linspace(0, 40, 1000) # start, finish, n points
#Estas son las ecuaciones que vamos a evaluar
d_r = 2.5 * tiempo
d_s = 3 * (tiempo-5)
#Código para graficar la solución
figura, ejes = plt.subplots()
plt.title('A Bank Robber Caught')#Título en la gráfica
plt.xlabel('time (in minutes)')#Título en el eje x
plt.ylabel('distance (in km)')#Título en el eje y
#Limita hasta donde va llegar el límite de la grafica en x , y
ejes.set_xlim([0, 40])
ejes.set_ylim([0, 100])
#Graficas de cada una de las ecuaciones
ejes.plot(tiempo, d_r, c='green')#d
ejes.plot(tiempo, d_s, c='brown')
#Lineas de intersección perpendiculares a x o y
plt.axvline(x=30, color='purple', linestyle='--')
_ = plt.axhline(y=75, color='purple', linestyle='--')
# Esta es muy importante porque va a mostrar la gráfica
plt.show()