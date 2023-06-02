nombres = ['Ana', 'Hugo', 'Valeria']
edades = [65,29,42]
ciudades = ['Lima', 'Buenos Aires', 'CDMX']
combinado = list(zip(nombres,edades,ciudades))
print(combinado)

for nombres,edades,ciudades in combinado:
    print(f'{nombres} tiene {edades} años y vive en {ciudades}')
