class Conta:
    def __init__(self, numero, cpf, nomeTitular, saldo):
        self.numero = numero
        self.cpf = cpf
        self.nomeTitular = nomeTitular
        self.saldo = saldo

    def setNumero(self, numero):
        self.numero = numero

    def setNumero(self, cpf):
        self.cpf = cpf

    def setNumero(self, nomeTitular):
        self.nomeTitular = nomeTitular

    def setNumero(self, saldo):
        self.saldo = saldo

    def get_numero(self):
        return self.numero

    def get_cpf(self):
        return self.cpf

    def get_nomeTitular(self):
        return self.nomeTitular

    def get_saldo(self):
        return self.saldo

    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        self.saldo -= valor


conta = Conta(1, "123456789-00", "Gustavo JB", 10000)
print(conta.get_nomeTitular())
print(conta.get_cpf())
print(conta.get_numero())
print(conta.get_saldo())

conta.depositar(220)
print(conta.get_saldo())
conta.sacar(120)
print(conta.get_saldo())
