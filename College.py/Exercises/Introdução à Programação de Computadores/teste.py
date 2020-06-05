p = 0
k = 0
a = int(input(f'Digite a idade do primeiro homem = '))
b = int(input(f'Digite a idade do segundo homem = '))
c = int(input(f'Digite a idade da primeira mulher = '))
d = int(input(f'Digite a idade da segunda mulher = '))
if b > a:
    p = a
    a = b
    b = p
if d > c:
    k = c
    c = d
    d = k
soma1 = a + d
soma2 = b + c
print(f'Homem mais velho + mulher mais nova = {soma1}')
print(f'Mulher mais velha + homem mais novo = {soma2}')

