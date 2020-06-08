from random import randint as rd

arr = []
menor = 100
menor2 = 100

for i in range(20):
    arr.append(rd(1, 100))

print('=' * 80)
print(arr)
print('=' * 80)

arr.sort()

print(f'As duas menores notas são: {arr[0]} e {arr[1]}')

