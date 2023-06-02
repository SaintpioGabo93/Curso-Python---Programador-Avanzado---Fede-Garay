def devolver_distinto(a,b,c):
    suma = a+b+c
    lista = [a,b,c]
    if suma > 15:
        return max(lista)
    if suma < 10:
        return min(lista)
    else:
        lista.sort()
        return lista[1]

print(devolver_distinto(5,3,9))