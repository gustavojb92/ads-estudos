nome = "exemplo de string em python"
print(nome)

# Atribuição multipla

a, b = 1, 2
print("antes da troca")
print(f"a={a} b={b}")

temp = a
a = b
b = temp
print("primeira troca troca")
print(f"a={a} b={b}")

a, b = b, a
print("segunda troca troca troca")
print(f"a={a} b={b}")
