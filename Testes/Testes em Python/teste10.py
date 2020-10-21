from random import randint 

conjunto = set()

while len(conjunto) <= 5:
    conjunto.add(randint(1,60))

print(sorted(conjunto))
