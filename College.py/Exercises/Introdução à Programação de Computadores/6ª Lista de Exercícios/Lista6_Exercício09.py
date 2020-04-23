from random import randint

L = []

for i in range(10):    
    x = randint(1, 50)
    if x not in L:
        L.append(x)
    
print(L)