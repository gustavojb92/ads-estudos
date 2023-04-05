def entraNumero():
    try:
        return int(input('Digite um Número'))
    except ValueError:
        print("Entres com um valor válido")
        entraNumero()


entraNumero()
