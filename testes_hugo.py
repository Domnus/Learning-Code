notas = []
maior = []
menor = []
i = 0
cont1 = 0
cont2 = 0
while i<10:
    nota = (int(input('Digite sua nota')))
    if nota<0 or nota>10:
        print('invalida')
        continue
    else:
        notas.append(nota)
        i += 1

notas.sort()
maior = notas[-1]
menor = notas[0]

for i in notas:
    if i == menor:
        cont1 += 1
    elif i == maior:
        cont2 += 1
print('A menor nota foi {} e foram {} alunos que a tiraram'.format(menor, cont1))
print(' maior {} foram {}'.format(maior, cont2))