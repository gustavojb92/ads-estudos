a = 20
b = 30
maior = a
if (b > maior):
    maior = b
print(f"o maior numero é {maior}")

a = 20
if (a % 2 == 0):
    situacao = "é par"
else:
    situacao = "é impar"
print(situacao)

nota = int(input("Qual foi a nota do aluno "))

if (nota > 7):
    situacao = "aprovado"
elif (nota < 5):
    situacao = "reprovado"
else:
    situacao = "recuperação"
print(situacao)

preco = 10
quantidade = int(input("Quantas unidades deseja"))
descDez = 0.1
descVinte = 0.2
soma = quantidade * preco
if (quantidade <= 10):
    total = preco * quantidade
elif (quantidade <= 20):
    total = preco * quantidade * (1-descDez)
else:
    total = preco * quantidade * (1-descVinte)
print(f"total: {total}")
