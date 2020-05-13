from random import randint
matriz = [0] * 5
x = []
y = 1
for i in range(5):
    matriz[i] = [0] * 5
    for j in range(5):
        matriz[i][j] = randint(0, 9)

for i in matriz:
    print(i)

print('Triângulo Inferior Direito:')

for i in  range(1, 5):
    for j in range(5 - i, 5):
        x.append(matriz[i][j])
        if len(x) == y:
            print(x)
            x = []
            y += 1




