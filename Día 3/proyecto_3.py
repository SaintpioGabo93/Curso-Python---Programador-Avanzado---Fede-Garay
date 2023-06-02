texto = input('Ingresa un texto, ya sea un poema, un artículo, o lo que quieras: ')
letras = [] #Así se guarda una variable vacía

texto_min = texto.lower()

letras.append(input('Ingresa la primera letra: ').lower())#Agregas elementos a la variable vacía
letras.append(input('Ingresa la segunda letra: ').lower())
letras.append(input('Ingresa la tercera letra: ').lower())
print('\ ')
contador_0a = texto.count(letras[0])
contador_0b = texto.count(letras[1])
contador_0c = texto.count(letras[2])

palabras = texto.split()
primera_letra = texto[0]
ultima_letra = texto[-1::]
inverso = texto[::-1]

print(f'El texto que escribiste es: {texto}')
print(f'La cantidad de veces que se repite las letras {letras[0]}, {letras[1]} y {letras[2]} es: '
      f'{contador_0a}, {contador_0b} y {contador_0c}')
print(f'La cantidad de frases que hay en tu texto es: {len(palabras)}')
print(f'La primera letra de tu texto es: {primera_letra}')
print(f'La última es: {ultima_letra}')
print(f'El texto inverso se escribe: {inverso}')
print('Python' in texto)

