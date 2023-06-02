monedas = 5
while monedas > 0:
    print(f'Tengo {monedas} monedas')
    monedas -= 1
else:
    print('No tengo más dinero')

respuesta = 's'
while respuesta == 's':
    respuesta = input('¿Deseas continuar? s/n')
else:
    print('Gracias')


nombre = input('Escribe un nombre: ')
for n in nombre:
    if n == 'i':
        break
    print(n)

nombre2 = input('Escribe un nombre: ')
for k in nombre2:
    if k == 'e':
        continue #Esto hará que se salte esa linea y no se imprima
    print(k)

prueba = 'k'
while prueba == 'k':
    pass #Esta linea ayuda a que este código no se ejecute y se pueda programar después
print('Se voló el loop while, :v')