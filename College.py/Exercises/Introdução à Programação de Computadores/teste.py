from random import randint

Lista = []
l = []
for i in range(50):
    Lista.append(randint(1, 101))
print('A lsita é',Lista)
cond = True
while cond:
        x = int(input('Digite o valor de X:'))
        if x > 49 or x < 0:
            print('Digite um valor entre 0 e 49!')
            continue 
        else:
            y = int(input('Digite o valor de Y:'))
            if y > 49 or y < 0:
                print('Digite um valor entre 0 e 49"!')  
                continue
            else:
                if y < x:
                    print('O valor de X deve ser menor que o Y!')
                else:
                    for i in range(x, y):
                        posiçao = Lista[i]
                        l.append(posiçao)
                    cond = False
    
print(f'A lista nova é {l}')