def suma(**kwargs):
    for clave,valor in kwargs.items():
        print(f'{clave} = {valor}')

suma(x=3, y=4, z=5)

#También se puede

def suma_0(**kwargs):
    total = 0
    for clave, valor in kwargs.items():
        total += valor
    return total
print(suma_0(x=3, y=4, z=5))

def suma_1(num1,num2,*args,**kwargs):
    print(f'El primer valor es {num1}')
    print(f'El segundo valor es {num2}')

    for arg in args:
        print(f'arg = {arg}')

    for clave,valor in kwargs.items():
        print(f'{clave} = {valor}')

print(suma_1(1,2,5,98,59, k='uno', m='dos', p='tres'))
