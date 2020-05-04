from random import randint

A = []
B = []
C = []

for i in range(10):
    A.append(randint(1, 10))

for i in range(10):
    B.append(randint(1, 10))


for i in A:
    for j in B:
        if i == j:
            C.append(i)

print(A)
print(B)
print(C)
