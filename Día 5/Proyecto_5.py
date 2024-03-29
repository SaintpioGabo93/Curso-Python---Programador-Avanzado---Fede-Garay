from random import choice

palabras = ['panadero','dinosaurio','helipuerto','tiburon'] #Primero se declaran las variables que se van a utilizar
#según el diagrama de flujo
letras_correctas = []
letras_incorrectas = []
intentos = 6
aciertos = 0
juego_terminado = False

def elegir_palabras(lista_palabras): #Esto nos dira que hace falta una variable
    palabra_elegida = choice(lista_palabras)
    letras_unicas = len(set(palabra_elegida))#Contendrá como información cuantas letras distintas hay en la palabra sin importar las repeticiones
    return palabra_elegida, letras_unicas

def pedir_letra():#el parámetro está vacio porque no necesita nada para que suceda
    letra_elegida = ''
    es_valida = False
    abecedario = 'abcdefghijklmnñopqrstuzwxyz'

    while not es_valida:
        letra_elegida = input('Elige una letra: ').lower()
        if letra_elegida in abecedario and len(letra_elegida) == 1:
            es_valida = True
        else:
            print('No has elegido una letra valida')

    return letra_elegida

def mostrar_nuevo_tablero(palabra_elegida):
    lista_oculta = []
    for l in palabra_elegida:
        if l in letras_correctas:
            lista_oculta.append(l)
        else:
            lista_oculta.append('-')

    print(' '.join(lista_oculta))

def chequear_letra(letra_elegida,palabra_oculta,vidas,coincidencias):
    fin = False
    if letra_elegida in palabra_oculta and letra_elegida not in letras_correctas:
        letras_correctas.append(letra_elegida)
        coincidencias += 1
    elif letra_elegida in palabra_oculta and letra_elegida not in letras_correctas:
        print('Ya elegiste esta letra, prueba con otra')
    else:
        letras_incorrectas.append(letra_elegida)
        vidas -= 1
    if vidas == 0:
        fin = perder()
    elif coincidencias == letras_unicas:
        fin = ganar(palabra_oculta)
    return vidas, fin,coincidencias

def perder():
    print('Se te acabaron las vidas')
    print('La palabra oculta era: '+palabra)
    return True
def ganar(palabra_descubierta):
    mostrar_nuevo_tablero(palabra_descubierta)
    print('Felicitaciones, has encontrado la palabra!!!')
    return True

palabra, letras_unicas = elegir_palabras(palabras) #Invocamos a la función elegir_palabras y esta tiene que estar alimentada por una lista,
                          #que es la lista de palabras que hicimos al principio
while not juego_terminado:
    print('\n'+'*'*20+'\n')
    mostrar_nuevo_tablero(palabra)
    print('\n')
    print('Letras incorrectas: '+'-'.join(letras_incorrectas))
    print(f'Vidas: {intentos}')
    print('\n' + '*' * 20 + '\n')
    letra = pedir_letra()

    intentos,terminado,aciertos = chequear_letra(letra,palabra,intentos,aciertos)
    juego_terminado = terminado