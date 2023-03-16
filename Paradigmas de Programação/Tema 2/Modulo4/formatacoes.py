hora = 10
minutos = 26
segundos = 18

print("{}:{}:{}" .format(hora, minutos, segundos))
print(f"{hora}:{minutos}:{segundos}")

# Também é possível especificar a largura de campo para exibir um inteiro.
# Se a largura não for especificada, ela será determinada pela
# quantidade de dígitos do valor a ser impresso

print("{:4}, {:5}".format(10, 100))
print("{:8.5}".format(10/3))

# Também é possível imprimir a string como lida da direita para a esquerda.
# Para isso, deve-se utilizar [: : -1].
# Esse valor -1 indica que a leitura dos caracteres será
# feita no sentido oposto ao tradicional.

str = "olá mundo"
print(str[::-1])
