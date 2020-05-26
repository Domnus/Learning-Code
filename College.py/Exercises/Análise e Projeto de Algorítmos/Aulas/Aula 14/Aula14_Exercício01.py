arr = [0] * 8

for i in range(8):
    arr[i] = [0] * 8
    
while True:
    x, y = input('Informe as coordenadas da Torre [0 a 7] -> ').split(',')
    x = int(x)
    y = int(y)
    if x not in range(8) or y not in range(8):
        print('Coordenadas erradas! Digite um valor entre 0 e 7!')
    else:
        break

for i in range(8):
    for j in range(8):
        if i == x:
            arr[i][j] = 1
        if j == y:
            arr[i][j] = 1

for i in range(8):
    for j in range(8):
        print(f'[{arr[i][j]}]', end= '')
    print()