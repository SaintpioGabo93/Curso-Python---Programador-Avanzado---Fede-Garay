import numpy as np

x = np.array([25,2,5]) # Con esta notación no se puede transponer el vector
y = np.array([[25,2,5]]) # Si declaramos así el vector si se podrá transponer con los métodos de transposición de numpy
dimension_x = x.shape
dimension_y =y.shape
print(x)
print(y)
print(len(x))
print(len(y))
print(dimension_x)
print(dimension_y)
print(type(x))
print(type(y))
print(x[0]) # Ese como en una lista, nos va a mostrar qué valor tiene la posicion de ese vector
print(y[0])
print(type(x[0]))
print(type(x[0]))
# Transposición vectorial
vector_x_transnpuesto = x.T # Esta transposición vectorial no tendrá ningún efecto, porque no está declarado en su variable
#como una matríz
vector_y_transnpuesto = y.T # Este si se transpondrá porque está bien declarado
print(vector_x_transnpuesto)
print(vector_y_transnpuesto)
# Vectores cero
vector_cero = np.zeros(3)
print(vector_cero)