lista = ['a','b','c']
indice = 0
for item in lista:
    print(indice,item)
    indice += 1

lista_0 = ['a','b','c']

for item in enumerate(lista_0):
    print(item)

lista_0 = ['a','b','c']

for indice,item in enumerate(lista_0):
    print(indice,item)

lista_1 = ['a','b','c']

mis_tuples = list(enumerate(lista_1))
print(mis_tuples)