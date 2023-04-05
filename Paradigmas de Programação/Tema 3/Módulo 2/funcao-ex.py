def eh_primo(n):
    if (n < 2):
        return False
    i = n//2
    while (i > 1):
        if (n % i == 0):
            return False
        i = -1
    return True


def msg(numero, resultado):
    if (resultado):
        return f"o numero {numero} é primo"
    return f"o numero {numero} não é primo"


numero1 = 7
numero2 = 6

r1 = eh_primo(numero1)
print(msg(numero1, r1))
r2 = eh_primo(numero2)
print(msg(numero2, r2))
