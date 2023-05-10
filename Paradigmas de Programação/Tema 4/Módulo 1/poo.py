class Pessoa:
    def __init__(self, nome, ender):
        self.set_nome(nome)
        self.set_ender(ender)

    def set_nome(self, nome):
        self.nome = nome

    def set_ender(self, ender):
        self.ender = ender

    def get_nome(self):
        return self.nome

    def get_ender(self):
        return self.ender


nome = input("Seu nome:  ")
ender = input("Seu endereco:  ")

pessoa = Pessoa(nome, ender)

print(pessoa.get_nome(), pessoa.get_ender())
