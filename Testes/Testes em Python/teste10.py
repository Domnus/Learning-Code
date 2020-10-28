alf = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
entr = input('Insira a palavra desejada : ').upper()
qtd = int(input('Insira a quantidade de vezes que deseja mover a letra : '))
out = ''
for i in entr:
    x = alf.index(i) + qtd
    while x >= 27:
        x -= 27
    y = alf[x]
    out += y

print('Palavra criptografada : {}'.format(out))
