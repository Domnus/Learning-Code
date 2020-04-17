k = int(input('Função Resto -> '))
m = int(input('-> '))

if k > 0:
    result = k % m
if k < 0:
    result2 = (k * -1) % m
    result = m - result2
print(result)
