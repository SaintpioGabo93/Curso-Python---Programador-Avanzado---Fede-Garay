mi_set = set([1,2,3,4,5]) #Es importante encerrar los números entre paréntesis o comillas
#si es usa esta forma de declarar
print(type(mi_set))
print(mi_set)
otro_set ={1,0,3,5} #Con esta forma, no es necesario encerrar en doble paréntesis, si están desordenados
#cuando los imprime se ordendan, y descarta numeros o caracteres repetidos
print(type(otro_set))
print(otro_set)
set_2 = {1,2,5,9,(5,6.6,9),8,6} #Los sets no admites listas ni diccionarios pero tuples, sí.
print(set_2)
print(len(mi_set))
print(len(set_2))
print(2 in mi_set)
s1 = {1,2,3}
s2 = {3,4,5}
s3 = s1.union(s2)
print(s3)
s4 = {1,2,3}
s4.add(5)
print(s4)
s4.remove(2)
print(s4)
s4.discard(7) #También elimina como remove, pero no te manda error si pones un elemento que
#no exista en el set
elem_desc = s4.pop() #Elimina un elemento aleatorio
print(s4)
print(elem_desc)
s4.clear() #convierte el set en un conjunto vacío.
