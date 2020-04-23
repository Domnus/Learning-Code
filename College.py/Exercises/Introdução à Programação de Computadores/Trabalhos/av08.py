from random import randint

L = []
l = []
for i in range(50):
    L.append(randint(1, 50))
print(L)

print('Digite duas posições da lista: (0 a 49)')




x = True

while x:
        x = int(input('-> '))
        if x > 49 or x < 0:
            print('Número inválido!')
            continue 
        else:
            y = int(input('-> '))
            if y > 49 or y < 0:
                print('Número inválido!')  
                continue
            else:
                if y < x:
                    print('O primeiro número deve ser menor que o segundo!')
                else:
                    while x <= y:
                        i = L[x]
                        l.append(i)
                        x += 1
                    x = False
    
print(l)


                

