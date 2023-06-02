import numpy as np
# Norma Euclidiana o R_2
x = np.array([25,2,5])
norma_euclidiana_sin_tanta_mamada = np.linalg.norm(x)
tambien_norma_sin_ser_mamador = ((25**2 + 2**2 + 5**2)**0.5)
def norma_euclidiana(lista):
    i=0
    for l in x:
        i += l**2

    return i

# Norma R_1
def norma_r_1(lista):
    i = 0
    for l in x:
        i += abs(l)

    return i
def norma_al_infinito(lista):
    i = max(lista)
    return i

print(f'Este es el resultado para la norma al cuadrado de un vector = {norma_euclidiana(x)}')
print(f'Esta es la norma euclidiana, en el código aparece como una función = {norma_euclidiana(x) ** 0.5}')
print(f'Esta es la norma euclidiana, en el código se manipula con un método el método'
      f' np.linalg.norm(lista) = {norma_euclidiana_sin_tanta_mamada}')
print(f'Esta norma se declara de manera tosca, sólo se declara'
      f'los valores del vector y sus operaciones en una variable = {tambien_norma_sin_ser_mamador}')
print(f'Esta es la norma en R_1 del vector, simplemente es la suma de '
      f'distancias de cada vector = {norma_r_1(x)}')
print(norma_al_infinito(x))

