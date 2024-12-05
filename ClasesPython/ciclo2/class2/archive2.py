class cuentaBancaria:
    
    def __init__(self, titular, saldo , clave):
        self.titular = titular
        self._saldo = saldo
        self.__clave = clave
    
    def depositar(self, cantidadDeposito):
        self._saldo += cantidadDeposito
        return f"deposito exitoso, saldo actual {self._saldo}"
    
    def retirar(self, cantidadRetiro):
        if cantidadRetiro > self._saldo:
            return "fondos insuficientes"
        self._saldo -= cantidadRetiro
        return f"retiro exitoso, el saldo actual es {self._saldo}"
    
    def modificarClave(self, nuevaClave):
        self.__clave = nuevaClave
        return f"clave solicitada de forma exitosa, la nueva clave es {self.__clave}"
    
cuentaBancaria1 = cuentaBancaria("Luis Guillermo", 1000000, 1234)

print(cuentaBancaria1.titular)
print(cuentaBancaria1._saldo)

print(cuentaBancaria1.depositar(500000))
print(cuentaBancaria1.depositar(500000))
print(cuentaBancaria1.retirar(200000))
print(cuentaBancaria1.retirar(200000))
print(cuentaBancaria1.retirar(200000))
print(cuentaBancaria1.retirar(200000))
print(cuentaBancaria1.retirar(200000))

print(cuentaBancaria1.modificarClave(11200230))
