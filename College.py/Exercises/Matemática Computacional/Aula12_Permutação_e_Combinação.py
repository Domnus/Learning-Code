from math import factorial

rep = {}
k = 0
fact = 1

C_ou_P = input('Combinação ou Permutação? ').upper()[0]

if C_ou_P == 'C':
    print('-----Combinação-----')
    n = int(input('-> '))
    r = int(input('-> '))
    C = factorial(n) / (factorial(r) * factorial(n - r))
elif C_ou_P == 'P':
    print('-----Permutação-----')
    n = int(input('-> '))
    r = int(input('-> '))
    if n > r:
        C = factorial(n) / factorial(n - r)
    elif n == r:
        while True:
            print('Insira o número de repetições de elementos: ')
            value = int(input('-> '))
            key = k
            rep[k] = value
            x = input('Deseja adicionar mais números? [S/N]: ').upper()[0]
            if x == 'N':
                for i in rep:
                    fact *= factorial(rep[i])
                C = factorial(n) / fact 
                break
            else:
                k += 1

print(C)