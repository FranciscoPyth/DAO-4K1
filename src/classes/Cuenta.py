class Cuenta:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo

    
    def __str__(self):
        return f"{self.titular} - {self.saldo}"
    

    def saldo(self):
        return self.saldo
    

    def depositar(self, monto):
        self.saldo += monto


    def extraer(self, monto):
        if monto <= self.saldo:
            self.saldo -= monto
        else:
            print("No hay saldo suficiente")