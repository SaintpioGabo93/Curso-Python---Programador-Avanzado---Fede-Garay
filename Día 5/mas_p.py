def describir_persona(nombre, **kwargs):
    print(f'Características de {nombre}: ')
    for nombre_argumento, valor_argumento in kwargs.items():
        print(f'{nombre_argumento}: {valor_argumento}')


print(describir_persona("María", color_ojos="azules", color_pelo="rubio"))

def describir_persona(nombre, **kwargs):
    print(f"Características de {nombre}:")
    for clave, valor in kwargs.items():
        print(f'{clave}: {valor}')
