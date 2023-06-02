lista_0 = ['a', 'b', 'c', 'd']
for letra in lista_0: #La primera parte del for habla de los elementos en la variable lista
    numero_letra = lista_0.index(letra) + 1 #Se pueden usar métodos e imprimirlos
    print(f'Letra {numero_letra}: {letra}')
print('\n')#Para dar un salto de linea en el código
lista_1 = ['Pablo', 'Laura', 'Fede', 'Luis', 'Julia']
for nombre in lista_1:
    if nombre.startswith('L'):
            print(nombre)
    else:
        print('Nombre que no comienza con L')
print('\n')
numeros = [1,2,3,4,5]
i = 0

for numero in numeros:
    i = i + numero #Tomaraá el valor de i = 0, y lo sumará al de la lista, para la siguiente iteración el valor de i
    #será el de la iteración anteriar y se le sumará el siguiente valor de la lista
    print(i)

print('\n')

p = 'Python'

for letra in p: #Así se puede imprimir cada caracter del string de la variable
    print(letra)

print('\n')

for letra in 'Python': #Se puede escribir directamente lo que querramos en la iteración
    print(letra)

print('\n')

for objeto in [[1,2],[3,4],[5,6]]: #Se pueden escribir listas, tuples, diccionarios, sets, etc.
    print(objeto)

print('\n')

for a,b in [[1,2],[3,4],[5,6]]: #Con las variables a  y b, se le asigna una posición a cada lista de la lista
    print(a)
    print(b)

print('\n')

for item in {'c1':'a','c2':[1,2],'c3':{'s1':'hola', 's2':3.1416}}: #Esta solo imprimirá la clave del diccionario
    print(item)

print('\n')

for item in {'c1':'a','c2':[1,2],'c3':{'s1':'hola', 's2':3.1416}}.items():#Esta imprimirá la clave y lo que tiene la clave
    print(item)

print('\n')

for item in {'c1':'a','c2':[1,2],'c3':{'s1':'hola', 's2':3.1416}}.values():#Esta imprimirá sólo el contenido de la clave
    print(item)
print('\n')
#Una manera más sencilla de verlo
dic = {'c1':'a','c2':[1,2],'c3':{'s1':'hola', 's2':3.1416}}
for item in dic:
    print(item)

for item in dic.items():
    print(item)

for item in dic.values():
    print(item)
#De igual manera se pueden separar las claves con su contenido
print('\n')
dic2 = {'c1':'a','c2':[1,2],'c3':{'s1':'hola', 's2':3.1416}}
for a,b in dic2.items():
    print(a,b)

