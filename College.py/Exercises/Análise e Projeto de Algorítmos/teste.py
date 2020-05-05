from random import randint
a = 'sim'
L = []
while a == 'sim':
    for i in range(10):
        L.append(randint(1,50))

    print('Digite 1 para mostrar em ordem normal \nDigite 2 para mostrar em ordem inversa')

    while True:
        x = int(input('Digite o numero: '))
        if x == 1:
            print(L)
            break
        elif x == 2:
            L.reverse()
            print(L)
            break
        else:
            print('Numero invalido')
            continue

    a = input('Deseja repetir? [Sim/Nao] ')
    a = a.lower()
    
    

        