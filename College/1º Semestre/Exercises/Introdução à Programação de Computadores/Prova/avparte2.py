n = int(input('Digite o valor de n: '))
arr = [0] * n
nulo = 0
valid = None
print('Digite os valores da Matriz:')

for i in range(n):
    arr[i] = [0] * n
    for j in range(n):
        arr[i][j] = int(input('-> '))

for i in range(n):
    for j in range(n):
        print(f'[{arr[i][j]:2}]', end=' ')
    print()

for i in range(n):
    for j in range(n):
        if arr[j][i] != 0:
            valid = False
        else:
            valid = True
    if valid:
        nulo += 1

if nulo == 0:
    print('Não há colunas nulas na matriz')
if nulo == n:
    print('A Matriz inteira é nula')
else:
    print(f'Há {nulo} colunas nulas na Matriz')