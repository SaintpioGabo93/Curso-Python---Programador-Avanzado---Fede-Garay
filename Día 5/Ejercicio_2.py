txt = input('Ingresa un texto: ')
def inversor_texto(txt):
    convertidor = set(txt)
    r = list(convertidor).sort()
    return r

comprobador = inversor_texto(txt)
print(comprobador)