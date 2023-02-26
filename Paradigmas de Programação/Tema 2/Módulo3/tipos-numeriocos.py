# inteiro
a = 1_000_000_000
print(a)
print(type(a))

# float ou decimal
a = 5.00
print(a)
print(type(a))

"""
 Ao usar a vírgula como separador em Python, 
 o que ocorre, na verdade, é a criação de uma tupla de dois elementos, 
 e não o tipo float.
"""

# Exponenciação
a = 2**22
print(a)
print(type(a))
a = 2.0**22
print(a)
print(type(a))

x = 5 / 2
print(x)
print(type(x))

"""
Para obter o quociente inteiro e resto, 
quando dois inteiros são divididos, 
é necessário utilizar os operadores // e %, respectivamente. 
Ao dividir 21 por 2, temos quociente 10 e resto 1. Observe no box a seguir.
"""

x = 21 // 2
print(x)
x = 21 % 2
print(x)

# tipos complexos

r = complex(2, 5)
print(r)
q = r.conjugate()
print(q)
s = 2 + 5j
print(type(s))

# tipo bool

x = 2 < 3
print(x)
print(type(x))
x = not (2 < 3)
print(x)
print(type(x))

a = 2 + 3 - 4**2 + 5 / 2 - 5 // 2
print(a)

a = ["U"] + ["RN"]
print(a)
print(len(a))
b = ["4"] * 4
print(b)
print(len(b))
