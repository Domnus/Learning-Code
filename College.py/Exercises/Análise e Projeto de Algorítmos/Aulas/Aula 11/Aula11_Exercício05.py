from random import randint

A = []
print('Informe 10 elementos:')
for i in range(10):
    A.append(int(input('->')))

A.sort()

print(A)