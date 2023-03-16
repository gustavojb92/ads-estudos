numeros = [0, 0, 0, 0, 0]
count = 0
while (count < 5):
    numeros[count] = int(input("digite um numero"))
    count += 1
total = 0
for i in range(len(numeros)):
    total += numeros[i]
print(numeros)
print(total)
