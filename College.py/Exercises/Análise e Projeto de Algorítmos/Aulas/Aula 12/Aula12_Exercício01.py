from random import randint
matriz = [0] * 5

for i in range(5):
    matriz[i] = [0] * 5
    for j in range(5):
        matriz[i][j] = randint(0, 9)

for i in matriz:
    print(i)

print('Diagonal Secundária:')
for i in range(5):
    print(matriz[i][4-i])
    