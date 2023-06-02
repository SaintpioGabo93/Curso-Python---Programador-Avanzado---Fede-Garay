from random import *
num_rand = randint(1,101)
nombre = input('Escribe tu nombre: ')
print(f'¡Hola, {nombre}! Vamos a jugar un juego, '
      f'he pensado en un número del 1 al 100, vamos a ver si lo adivinas, tienes 8 intentos')

intentos = 10
while intentos > 0:
    num_usuario = input('Escribe un número: ')
    if int(num_usuario) == int(num_rand):
        print(f'¡Felicidades, {nombre}. Ganaste!')
        break
    elif int(num_usuario) > int(num_rand):
        print(f'Los siento {nombre}, el numero que elegí es menor')
        intentos-=1
    elif int(num_usuario) < int(num_rand):
        print(f'Los siento {nombre}, el numero que elegí es mayor')
        intentos -=1

else:
    print(f'Lo sentimos {nombre}, te quedan {intentos} intentos, perdiste, :B')