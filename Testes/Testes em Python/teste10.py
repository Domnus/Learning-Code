def menu():
    print('Opção 1 = Inserção')
    print('Opção 2 = Consulta')
    print('Opção 3 = Listagem')
    print('Opçao 4 = Sair')
    opção = int(input('informe uma opçao - >'))
    return opção


def inserção(cor, numero):
    rgb.append((cor, numero))
    return rgb


def consulta():
    cor = input('informe a cor - >').upper()
    for i in range(len(rgb)):
        if cor in rgb[i]:
            return f'{rgb[i]} \n'
    return 'Cor Não Cadastrada \n'


def lista():
    return f'{rgb}'


rgb = []

while True:
    opção = menu()
    if opção == 1:
        cor = input('informe a cor - >').upper()
        numero = input('informe o numero da cor ->')
        inserção(cor, numero)
    elif opção == 2:
        print(consulta())
    elif opção == 3:
        print(lista())
    elif opção == 4:
        print('TA MUITO QUENTE')
        break
    else:
        print('invalido')
