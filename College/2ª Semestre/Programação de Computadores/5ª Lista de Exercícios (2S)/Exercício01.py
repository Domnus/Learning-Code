def elevar(numero, expoente):
    if expoente == 0:
        return 1
    return numero * elevar(numero, expoente - 1) 

print(elevar(2, 10))