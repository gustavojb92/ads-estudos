# forma 1

def fatorial_interativo(n):
    f = 1
    for i in range(1, n+1):
        f = f*i
    return f

# forma 2


def fatorial_recursiva(n):
    if ((n == 0) or (n == 1)):
        return 1
    return n * fatorial_recursiva(n-1)


numero = 5

print(fatorial_interativo(numero))
print(fatorial_recursiva(numero))
