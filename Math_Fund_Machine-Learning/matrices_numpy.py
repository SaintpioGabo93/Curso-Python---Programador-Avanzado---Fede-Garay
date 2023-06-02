import numpy as np
X = np.array([[25,2],[5,26],[3,7]])
dimensiones = X.shape
no_elementos = X.size
seleccion_columna1 = X[:,0]
seleccion_columna2 = X[:,1]
#seleccion_columna3 = X[:,2] # Esta me va a arrojar error porque en filas no existe el indice 2
seleccion_f = X[0,:] # Así se selecciona la fila
seleccion_f_c = X[1:3,0:3] # X[indice en el que inicia:hasta que fila va a llegar,

# Operaciones:

transposicion = X.T
mult = X*2
sum_mat = X+2 # El 2 hace una matríz con ese numero de la misma dimension de la matriz X
mult_sum = X*2+2
# Impresiones:

print(X)
print(dimensiones)
print(no_elementos)
print(seleccion_columna1)
print(seleccion_columna2)
#print(seleccion_columna3)
print(seleccion_f)
print(seleccion_f_c)

# Impresiones de operaciones:

print(transposicion)
print(mult)
print(sum_mat)
print(mult_sum)


