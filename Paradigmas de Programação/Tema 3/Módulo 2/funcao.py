def encontrar_minimo(lista):
    minimo = lista[0]
    for elem in lista:
        if (elem < minimo):
            minimo = elem

    return minimo


listaA = [5, 6, 7, 8, 9, 4, 34, 6, 675]

listaB = [54, 56747, 23424, 8765856, 34244578, 8786673, 453]

menorA = encontrar_minimo(listaA)
menorB = encontrar_minimo(listaB)

print(f"menor da lista A {menorA}")
print(f"menor da lista B {menorB}")
