mi_bool = (4 < 5) and (5 == 2+3)
print(mi_bool)
mi_bool2 = (55 == 50) and ('perro' == 'perro') #Esta va a salir False, porque se tienen que cumplir las dos condiciones
print(mi_bool2)
mi_bool3 = (1 == 10) or (3==3) #Esta saldrá True, porque se tiene que cumplir sólo una de las dos condiciones
print(mi_bool3)
texto = 'Esta frase es breve'
mi_bool4 = ('frase' in texto) or ('Python' in texto) #En esta buscará en la variable texto, el resultado será True
print(mi_bool4)
mi_bool5 = not'a' == 'a' #También se puede utilizar De Morgan
print(mi_bool5)