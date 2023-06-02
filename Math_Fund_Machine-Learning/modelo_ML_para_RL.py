import torch
import matplotlib.pyplot as plt

x = torch.tensor([0,1,2,3,4,5,6,7]) # Dosis de medicamento
y = -0.5*x + 2 + torch.normal(mean=torch.zeros(8), std=0.5)


# y = torch.tensor([1.86, 1.31, .62, .33, .09, -.67, -1.23, -1.37])  #Relación dosis con el porcentaje de efectividad


fig, ax = plt.subplots()
plt.title('Pruebas clínicas')
plt.xlabel('Dosis de Medicamento')
plt.ylabel('Efectividad del Medicamento')
_ = ax.scatter(x,y)
plt.show()
# Formamos los parámetros para una recta cualquiera que se usará para la regresión lineal

m = torch.tensor([0.9]).requires_grad_()
b = torch.tensor([0.1]).requires_grad_()


def regresion(mi_m,mi_x,mi_b):  # mi_m corresponde a la pendiente, mi_x a al variable ind., mi_b a la raíz.
    return mi_m*mi_x + mi_b  # <---Ecuación de la recta


def grafica_regresion(mi_x,mi_y,mi_m, mi_b):

    fig, ax = plt.subplots()
    ax.scatter(mi_x, mi_y)

    x_min, x_max = ax.get_xlim()
    y_min = regresion(x_min, mi_m, mi_b).detach().item()
    y_max = regresion(x_max, mi_m, mi_b).detach().item()

    ax.set_xlim([x_min, x_max])
    _ = ax.plot([x_min, x_max], [y_min, y_max])


grafica_regresion(x, y, m, b)
plt.show()

# Pasos para Machine Learning

y_de_ajuste = regresion(x, m, b)  # Paso 1: Forward pass
print(y_de_ajuste)


def mse(mi_y_de_ajuste, mi_y):  # Paso 2: Comparación
    sigma = torch.sum((mi_y_de_ajuste - mi_y)**2)
    return sigma/len(mi_y)


C = mse(y_de_ajuste, y)
C.backward()  # Regresa a la función Seguimos paso 2
print(C)
grad_m = m.grad  # Estos son sólo para mostrar el resultado
print(grad_m)
grad_b = b.grad  # Ya están operados, solo hay que meterlos en el optimizador
print(grad_b)
optimizador = torch.optim.SGD([m, b], lr=0.01)
optimizador.step()
grafica_regresion(x, y, m, b)
plt.show()
C = mse(regresion(x, m, b), y)
print(C)  # Confirmamos que el gradiente del tensor ya descendió y está más cerca de la regresión

epochs = 1000
for epoch in range(epochs):
    optimizador.zero_grad()  # Este comando resetea el trabajo y volvemos a tener el tensor original
    y_de_ajuste = regresion(m, x, b)  # Paso 1: Regresiones
    C = mse(y_de_ajuste, y)  # Paso 2: Comparador
    C.backward()  # Paso 3: El valor del porcentaje se usa como valor inicial
    optimizador.step()  # Paso 4: Se deriva y obtiene el gradiente para entrenar el algoritmo para la RL
    print(f'Iteración o "Epoch": {epoch}, Coste: {C.item()}, gradiente de la pendiente{m.grad.item()}'
          f'gradiente de la raíz: {b.grad.item()}')

grafica_regresion(x, y, m, b)
plt.show()
print(f'Último gradiente de la pendiente: {m.item()}, último gradiente de la raiz: {b.item()}')
