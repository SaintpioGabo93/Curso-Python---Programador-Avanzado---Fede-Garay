#Esta es la libreria en para matemáticas
import numpy as np
import matplotlib.pyplot as plt
#Se declara la variable del tiempo
tiempo = np.linspace(-10, 10, 1000) # start, finish, n points
#Estas son las ecuaciones que vamos a evaluar
y_1 = 3 * tiempo
y_2 =1 + (5/2) * tiempo
#Código para graficar la solución
figura, ejes = plt.subplots()
plt.title('Sistema de ecuaciones')#Título en la gráfica
plt.xlabel('x')#Título en el eje x
plt.ylabel('y')#Título en el eje y
#Limita hasta donde va llegar el límite de la grafica en x , y
##ejes.set_xlim([0, 80])
##ejes.set_ylim([0, 100])
#Graficas de cada una de las ecuaciones
ejes.plot(tiempo, y_1, c='green')#d
ejes.plot(tiempo, y_2, c='brown')
#Lineas de intersección perpendiculares a x o y
# Esta es muy importante porque va a mostrar la gráfica
plt.show()