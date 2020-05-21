A = []
x = 0
cond = True
for i in range(3):
    A.append([])
    for j in range(3):
        while True:
            x = int(input('Digite os valores do Quadrado Mágico = '))
            if x < 2:
                print(f'Erro - Digite um valor acima de 2')
            else:
                A[i].append(x)
                break

print('Matriz:')        
for i in range(3):
    for j in range(3):
        print(f'[{A[i][j]}]',end= '')
    print()
        

