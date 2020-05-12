from random import randint
matriz = [0] * 5
x = []
y = 4

for i in range(5):
    matriz[i] = [0] * 5
    for j in range(5):
        matriz[i][j] = randint(0, 9)

for i in matriz:
    print(i)

print('Triângulo Inferior Direito:')

