from random import randint
aleatorio = randint(1,50) # Esto nos dará un número aleatorio en el intervalo cerrado de 1-49
print(aleatorio)

from random import * # Con este comando importamos toda la biblioteca de random, no se va a activar hasta que no declaremos un método de la biblioteca
aleatorio_0 = round(uniform(1,5),1) #Con este método se generará un número float aleatorio en el intervalo de 1 a 5, el parámetro fuera del intervalo del uniform es la cantidad de decimales que tendrá
print((aleatorio_0))

aleatorio_1 =random() #Generará un float en el intervalo abierto de 0 a 1
print(aleatorio_1)

numeros = [1,2,3,4,5,6,7,8,9]
aleatorio_2 = choice(numeros) # Este comando elegirá a un número aleatorio de la lista numeros
print(aleatorio_2)

mezcla = list(range(0,51,5))
print(mezcla)
shuffle(mezcla) # Este comando mezclará la lista del intervalo cerrado del 0 -50
print(mezcla)
