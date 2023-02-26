# variavel global
x = 1
print(x)

# variavel local


def multiplicador(numero):
    x = 2  # esta variável tem escopo local
    print(f"Dentro da função, a variável vale: {x}")
    return x * numero


x = 3  # esta variável tem escopo global
b = multiplicador(5)
print(f"Fora da função, a variável a vale: {x}")
print(f"b = {b}")


def multiplicador2(numero):
    return a * numero


a = 3  # esta variável tem escopo global
b = multiplicador2(5)
print(f"A variável b vale: {b}")


def multiplicador3(numero):
    global c  # todas as referências à variável a são para a global
    c = 2      # a global será alterado
    print(f"Dentro da função,  variável  vale: {c}")
    return c * numero


c = 3  # esta variável tem escopo global
b = multiplicador3(5)
print(f"A variável b vale: {b}")
print(f"Fora da função, a variável a vale: {c}")
