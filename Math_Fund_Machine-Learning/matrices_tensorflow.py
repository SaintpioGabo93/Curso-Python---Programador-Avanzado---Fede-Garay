import tensorflow as tf
X = tf.Variable([[25,2],[5,26],[3,7]])
rango = tf.rank(X)
dim = tf.shape(X)
seleccion_filas = X[1,:]

# Operaciones:
suma = int(X)+2

# Impresiones en pantalla:
print(X)
print(rango)
print(dim)
print(seleccion_filas)

# Impresiones Operaciones

print(suma)