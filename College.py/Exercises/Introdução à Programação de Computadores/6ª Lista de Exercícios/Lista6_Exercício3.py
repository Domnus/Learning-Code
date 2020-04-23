from random import randint

L = []

for i in range(20):
    L.append(randint(1,50))
print(L)

for n in L:
    if n % 5 == 0:
        
