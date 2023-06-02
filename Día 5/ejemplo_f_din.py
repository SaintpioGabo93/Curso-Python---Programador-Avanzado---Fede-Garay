# Ejemplo para desempacar un tuple
precios_cafe = [('Moka',15.5),('Americano',25.6),('Capuchino',40.5)]
#Desempacado normal
for cafe,precio in precios_cafe: #Estas instrucciones van a desempacar todos los precios
    print(cafe)
    print(precio)
# Con una función
def cafe_mas_caro (lista_precios):
    cafe_caro = ''
    precio_alto = 0

    for c,p in lista_precios:
        if p > precio_alto:
            precio_alto = p #Recorrerá toda la lista y si un valor de p es mayor que el precio más alto hasta ese momento
            # lo va a sobreescribir, si no es mayor, no hace nada
            cafe_caro = c #tomará el valor del tuple que tenga el valor más alto

        else:
            pass
    return (c,p)
print(cafe_mas_caro(precios_cafe))
