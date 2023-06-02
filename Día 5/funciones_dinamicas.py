def chequear_3_cifras_1(numero):
    return numero in range(100,1000)
resultado = chequear_3_cifras_1(658)
suma = 451 + 94
resultado_2 = chequear_3_cifras_1(suma)
print(resultado)
print(resultado_2)

def chequear_3_cifras_2(lista):
    for n in lista:
        if n in range(100,1000):
            return True
        else:
            pass
    return False
res = chequear_3_cifras_2([55,99,563,542])
print(res)

def chequear_3_cifras_3(lista):
    lista_3_cifras = []
    for n in lista:
        if n in range(100,1000):
            lista_3_cifras.append(n)
        else:
            pass
    return lista_3_cifras
res_2 = chequear_3_cifras_3([55,99,563,542])
print(res_2)
