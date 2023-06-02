import tensorflow as tf

x = tf.Variable(25)
y = tf.Variable(3)
# x = tf.Variable(25, dtype=  tf.int16) # dtype es opcional, tf es para qué tipo de int se usara si 16, 32, etc.
# y = tf.Variable(3, dtype=  tf.int16) # Para ambos se tiene que usar el mismo tipo de int, de lo contrario,
# arrojará error porque por defecto dtype es 32
dimension = x.shape
suma = x + y
suma_con_metodo = tf.add(x, y)
suma_solo_valor = suma_con_metodo.numpy

print(x) # Con las características de tensorflow nos va a imprimir en pantalla más información, esto es porque
         # La libreria tensorflow fue creada en C# para usarse en Python
print(dimension)
print(suma)
print(suma_con_metodo)
print(suma_solo_valor)