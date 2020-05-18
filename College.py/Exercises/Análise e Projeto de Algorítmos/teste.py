from random import randint

arr = [0] * 8
cont1 = 0
cont2 = 0

for i in range(8):
    arr[i] = [0] * 8
    for j in range(8):
        arr[i][j] = 0

for i in range(1, 8, 2):
    for j in range(1, 8, 2):
        arr[cont2][j] = 1
        arr[i][cont1] = 1   
        cont2 += 1
    cont1 += 1
    cont2 = 0
        
        
print('Matriz:')
print('=' * 24)
for i in range(8):
    for j in range(8):
        print(f'[{arr[i][j]}]', end='')
    print()
print('=' * 24)  