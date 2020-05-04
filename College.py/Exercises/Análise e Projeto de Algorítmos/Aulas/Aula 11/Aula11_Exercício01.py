A = []
a = 0
b = 0
'''
print('Digite 20 valores: ')
for i in range(20):
    A.append(int(input('-> ')))
'''
A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
print(A)

i = 0
while i <= 10:
    a = A[i]
    b = A[(i + 10)]
    a, b = b, a
    A.insert(i, a)
    A.insert((i + 10), b)
    i += 1
    print(A)
   
print(A)