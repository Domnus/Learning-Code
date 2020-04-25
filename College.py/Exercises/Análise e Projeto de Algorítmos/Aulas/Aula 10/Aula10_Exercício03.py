a = []
x = 1

print('Informe os valores abaixo: ')

while x <= 20:
    par_ou_impar = int(input('-> '))
    if par_ou_impar % 2 != 0:
        a.append(par_ou_impar)
        x += 1

print(f'Os 20 primeiros valores ímpares são: \n{a}')
    