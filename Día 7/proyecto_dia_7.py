class Persona:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido


class Cliente(Persona):
    def __init__(self, nombre, apellido, num_cuenta, balance=0):

        super().__init__(nombre, apellido)
        self.num_cuenta = num_cuenta
        self.balance = balance

    def __str__(self):
        return f'Cliente: {self.nombre} {self.apellido}\nBalance de cuenta: {self.num_cuenta}: ${self.balance} '

    def deposito(self, dep):
        self.balance += dep
        print('Deposito realizado con éxito')

    def retiro(self, ret):
        if self.balance >= ret:
            self.balance -= ret
            print('Retiro realizado con éxito')
        else:
            print('Fondos insuficientes')


def crear_cliente():
    nombre_cl = input("Ingrese su nombre: ")
    apellido_cl = input("Ingrese su apellido: ")
    num_cuenta = input("Ingrese su numero de cuenta: ")
    cliente = Cliente(nombre_cl,apellido_cl,num_cuenta)
    return cliente


def inicio():
    mi_cliente = crear_cliente()
    print(mi_cliente)
    opcion = 0

    while opcion != 'S':
        print('Elije: Depositar (D), Retirar (R), o Salir (S)')
        opcion = input()

        if opcion == 'D':
            monto_dep = int(input("Monto a depositar: "))
            mi_cliente.deposito(monto_dep)
        elif opcion == 'R':
            monto_ret = int(input("Monto a retirar: "))
            mi_cliente.retiro(monto_ret)
        print(mi_cliente)

    print("Gracias por operar en Banco Python")


inicio()
