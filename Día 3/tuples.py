mi_tuple = 1,2,3,4
tuple_muestra = 1,3.1416,'hola'
tuple_en_tuple = 1,2,(56,'murió',2.74),3,4
print(type(mi_tuple))
print(mi_tuple)
print(mi_tuple[1])
print(mi_tuple[-1])
print(tuple_en_tuple)
print(tuple_en_tuple[2])
print(tuple_en_tuple[2][1])
mi_tuple = list(mi_tuple) #Tuple a lista
print(type(mi_tuple))
mi_tuple = tuple(mi_tuple)
print(type(mi_tuple))

t = 1,2,3 #Esto te puede servir para tus matemáticas, krnal, :v

x,y,z = t
print(x,y,z)

a,b,c= tuple_muestra
print(a,b,c)

print(len(mi_tuple))
print(len(tuple_muestra))
print(len(tuple_en_tuple))

tuple_cont = 1,2,3,1,1,3,5
print(tuple_cont.count(1))
print(tuple_cont.index(3))

