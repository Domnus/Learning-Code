from random import randint

maior = 0
minimax = 50
arr = [0] * 5

for i in range(5):
    arr[i] = [0] * 5
    for j in range(5):
        arr[i][j] = randint(1, 50)

for i in range(5):
    for j in range(5):
        if arr[i][j] > maior:
            maior = arr[i][j]
            linha = i

print('Matriz:')
for i in range(5):
    for j in range(5):
        if arr[i][j] < 10:
            print(f'[0{arr[i][j]}]', end=' ')
        else:
            print(f'[{arr[i][j]}]', end=' ')
    print()


for i in range(5):
    if arr[linha][i] < minimax:
        minimax = arr[linha][i]

print(f'Maior número da matriz: {maior} | Linha {linha + 1}')
print(f'O menor número da linha {linha + 1} é o {minimax}')
