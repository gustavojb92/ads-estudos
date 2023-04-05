def soma_pares(lista):
    soma = 0
    for elem in lista:
        if (elem % 2 == 0):
            soma += elem
    return soma


lista = [2, 4, 5, 6, 7]

soma = soma_pares(lista)

print(f"a soma dos pares é {soma}")
