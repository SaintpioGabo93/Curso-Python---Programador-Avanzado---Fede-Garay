# Una vez que ya tenemos la estructura general
import os
from pathlib import  Path
from os import system

ruta = Path(Path.home(), 'Recetas')
print (ruta)

def contar_recetas(ruta): #Esta función contará el numero de recetas que tendrá el directorio según la ruta que le pasemos
    contador = 0
    for txt in Path(ruta).glob('**/*.txt'): # Buscará en la ruta que le pasemos todos los archivos con la terminacion txt
        contador += 1
    return contador

def inicio():
    ### Esta es la interfaz con la que interactuará el usuario
    system('cls')
    print('*'*50)
    print('*** Bienvenido al administrador de recetas ***')
    print('*'*50)
    print('\n')
    print(f'Las recetas se encuentran en {ruta}') # Así se enlaza  la interfaz gráfica con la ruta para las busquedas
    print(f'Total de recetas: {contar_recetas(ruta)}')
    ### Fin de la interfaz
    eleccion_menu = 'x'
    while not eleccion_menu.isnumeric() or int(eleccion_menu) not in range(1,7):
        print('Elige una opción: ')
        print('''
        [1] Leer Receta
        [2] Crear receta Nueva
        [3] Crear categoría nueva
        [4] Eliminar Receta
        [5] Eliminar Categoría
        [6] Salir del programa''')
        eleccion_menu =input()
    return menu
# inicio() para probar y ejecutar invocamos a la función

def mostrar_categorias(ruta):
    print('Categorías: ')
    ruta_categorias = Path(ruta)
    lista_categorías

menu = 0
if menu == 1: #Esta es la opción para leer una receta
    # mostrar categorías
    # elegir categoría
    # mostrar recetas
    # elegir receta
    # volver al inicio
    pass
elif menu == 2:
    # mostrar categorías
    # elegir categoría
    # crear receta nueva
    # volver al inicio
    pass

elif menu == 3:
    # mostrar categorías
    # elegir categoría
    # mostrar recetas
    # crear receta nueva
    # volver al inicio
    pass
elif menu == 4:
    # mostrar categorías
    # elegir categoría
    # mostrar recetas
    # eliminar receta
    # volver al inicio
    pass
elif menu == 6:
    # finalizar programa
    pass
