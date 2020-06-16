from random import randint
a = []
idosos = []
soma = 0
idade = []
somaidoso = 0
for i in range(20):
    idade = randint(1,80)
    a.append(idade)
    if idade>=65:
        idosos.append(idade)
        somaidoso+=1
        
for i in range(somaidoso):
    for j in range(i+1, len(idosos)):
        if idosos[j] < idosos[i]:
            idosos[j], idosos[i] = idosos[i], idosos[j]
            
for i in range(somaidoso):
    soma += idosos[i]
   
media = soma/(somaidoso)
print(a)
print('A media das idades é {:.2f}'.format(media))
print('O idoso mais novo tem {} anos'.format(idosos[0]))




'''
from random import randint as rd

M = []

for i in range(7):
    M.append([])
    for j in range(7):
        M[i].append(rd(0, 0))

for i in range(7):
    for j in range(7):
        if i <= j:
            M[i][j] = j ** 2
        else:
            M[i][j] = i ** 2

for i in range(7):
    for j in range(7):
        print(f'{M[i][j]:2}',end=" ")
    print()
    '''