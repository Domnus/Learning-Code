arr = [0] * 8
board = {'A':0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H':7}

for i in range(8):
    arr[i] = [0] * 8
    
while True:
    letra, y = input('Informe as coordenadas da Torre [0 a 7],[A a H] -> ').split(',')
    letra = letra.upper()
    x = board[letra]
    y = int(y)
    if x not in range(8) or y not in range(8):
        print('Coordenadas erradas! Digite um valor entre 0 e 7!')
    else:
        break

for i in range(8):
    for j in range(8):
        if arr[i][j] == arr[x][y]:
            arr[x][y] = 'T'
        elif i == x:
            arr[i][j] = 1
        elif j == y:
            arr[i][j] = 1

for i in range(8):
    for j in range(8):
        print(f'[{arr[i][j]}]', end= '')
    print()