def suma (*args):
    total = 0
    for arg in args: #El programa va a recorrer los valores ingresados por el usuario
        #Se inicializa una variable en cero para que pueda ir recorriendo los números y los
        #Vaya sumando
        total += arg #El argumento que haya ingresado el usiario se sumará a la variable total hasta
        #que recorra toda la tupla
    return total
print(suma(1,5,9,6,20))

def suma_2 (*args):
    return sum(args)

print(suma_2(1,5,9,6,20))