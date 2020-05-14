from random import randint

A = []
B = []
C = []
i = 0

print('Digite os números desejados:')

for i in range(6):
    num = randint(1, 60)
    if num not in B:
        A.append(num)


for i in range(7):
    x = int(input('Digite um numero'))
    if x < 1 or x > 60:
        print('Número inválido!')
        continue
    elif x in B:
        print('Número já digitado!')
    elif x not in B:
        B.append(x)