class Personaje:
    def __init__(self,no_flechas):
        self.cantidad_flechas = no_flechas

    def lanzar_flechas(self):
        self.cantidad_flechas = self.cantidad_flechas-1
        print(f'El tirador ahora tiene {self.cantidad_flechas}')
tirador = Personaje(10)
print(f'El tirador tiene {tirador.cantidad_flechas} flechas')
tirador.lanzar_flechas()



# Esta de abajo fue mi versión, está bien, pero es mejor la respuesta de arriba
class Personaje:
    def cantidad_flechas(self,no_flechas):
        self.cantidad_flechas = no_flechas

    def lanzar_flechas(self):
        self.cantidad_flechas = self.cantidad_flechas-1
        print(f'El tirador ahora tiene {self.cantidad_flechas}')
tirador = Personaje()
tirador.cantidad_flechas(10)
print(f'El tirador tiene {tirador.cantidad_flechas} flechas')
tirador.lanzar_flechas()