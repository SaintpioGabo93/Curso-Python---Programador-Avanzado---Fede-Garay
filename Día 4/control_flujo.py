if 10 > 9:
    print('Es correcto')

if True:
    print('Es correcto') #Aquí sólo se usa un booleano para demostrar que únicamente se busca que la condición sea
#Falsa o Verdadera
x = True #Es lo mismo pero se usa una variable booleana ya declarada
if  x:
    print('Así es... :B')

if 5 == 2:
    print('Es correcto')
else:
    print('No es correcto')

mascota = 'perro' #Cada elif evalúa si la condición se cumple, si no pasa al siguiente elif, hasta llegar al else
if mascota == 'gato':
    print('Así es...')
elif mascota == 'perro':
    print('Tienes un perro')
elif mascota == 'pez':
    print('Tienes un pez')
else:
    print('No sé qué mascota tienes')

edad = 16
calificacion = 9
if edad < 18:
    print('Eres mayor de edad')
    if calificacion >= 7: #Anidación de if
        print('Aprobado')
    else:
        print('Reprobado')
else:
    print('Eres adulto')