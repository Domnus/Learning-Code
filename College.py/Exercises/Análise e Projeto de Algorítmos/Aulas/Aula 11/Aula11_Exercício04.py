from random import randint

A = []
B = []
C = []

for i in range(10):
    A.append(randint(1, 10))

for i in range(10):
    B.append(randint(1, 10))

for i in A:
    C.append(i)
    
for i in B:
    for j in A:
        if j == i:
            
        else:
            C.append(i) 

print(A)
print(B)
print(C)