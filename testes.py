velha = """               Posições
   |   |      0 | 1 | 2
---+---+---  ---+---+---
   |   |      3 | 4 | 5
---+---+---  ---+---+---
   |   |      6 | 7 | 8
"""
print(velha)

matriz = ['','','',
          '','','',
          '','','']

print("Jogador 1 = X e Jogador 2 = O")

sair = "N"
repetir = 2
velha = 0

nomeUm = input("Digite o nome do primeiro jogador: ")
nomeDois = input("Digite o nome do segundo jogador: ")

while sair == "N":
    for i in range(20):
        if repetir % 2 == 0:

            linha = int(input(nomeUm + ", faça sua jogada: "))
            if matriz[linha] == '':
                matriz[linha] = 'X'
            else:
                print("Jogada inválida, tente novamente !")
                linha = int(input(nomeUm + ", faça sua jogada: "))
                matriz[linha] = 'X'

            print('\n %s | %s | %s ' % (matriz[0], matriz[1], matriz[2]))
            print('\n---------')
            print('\n %s | %s | %s ' % (matriz[3], matriz[4], matriz[5]))
            print('\n----------')
            print('\n %s | %s | %s ' % (matriz[6], matriz[7], matriz[8]))

        else:
            linha = int(input(nomeDois + ", faça sua jogada: "))
            if matriz[linha] == '':
                matriz[linha] = 'O'
            else:
                print("Jogada inválida, tente novamente !")
                linha = int(input(nomeDois + ", faça sua jogada: "))
                matriz[linha] = 'O'

            print('\n %s | %s | %s ' % (matriz[0], matriz[1], matriz[2]))
            print('\n---------')
            print('\n %s | %s | %s ' % (matriz[3], matriz[4], matriz[5]))
            print('\n----------')
            print('\n %s | %s | %s ' % (matriz[6], matriz[7], matriz[8]))

        repetir += 1

        if ((matriz[0] == matriz[1] == matriz[2] == 'X'),
            (matriz[3] == matriz[4] == matriz[5] == 'X'),
            (matriz[6] == matriz[7] == matriz[8] == 'X')):
            print(nomeUm + " foi o ganhador !!")
            break
        else:
            velha += 1

        if ((matriz[0] == matriz[1] == matriz[2] == 'O'),
            (matriz[3] == matriz[4] == matriz[5] == 'O'),
            (matriz[6] == matriz[7] == matriz[8] == 'O')):
            print(nomeDois + " foi o ganhador !!")
            break
        else:
            velha += 1

op = input('Deseja jogar novamente ? "S"-sim ou "N"-não : ')
if op == 'N':
    matriz = ['','','',
              '','','',
              '','','']