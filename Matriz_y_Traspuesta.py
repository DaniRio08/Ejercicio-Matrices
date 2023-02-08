import random
print()
print("La matriz es: ")
print()
matriz = []
for i in range(3):
    fila = []
    for j in range(3):
        fila.append(random.randint(1,9))
    matriz.append(fila)

for i in range (len(matriz)):
        for j in range (len(matriz[i])):
            print(matriz[i][j], end = " ")
        print()

print()
print("La matriz transpuesta es: ")
print()
for i in range (len(matriz)):
    for j in range (len(matriz[i])):
        print(matriz[j][i], end = " ")
    print()
print()