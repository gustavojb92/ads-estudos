print("Olá mundo!")
s = "Hello world!"
print(s)
num = 10
print(num)
nome = input("Qual é o seu nome?")
print("olá, ", nome)
# A função eval() recebe uma string, mas trata como um valor numérico
numero = input("digite um numero")
print(numero)
print(eval(numero))

# podemos tratar essa entrada para poder realizar operações numericas
numero = eval(input("Entre com um numero "))
x = numero + 2
print(numero, "+ 2 =", x)
