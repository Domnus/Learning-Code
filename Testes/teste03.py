# Emmanuel Miguel Tiede - RA:569453
from time import sleep
replay = 'S'
t = 3
jg1 = None
jg2 = None
cond = True
turno = 1
# -------------------------
while replay == 'S':
    # Inicia o programa
    turno = 1
    tabuleiro = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    print(f'Seu jogo esta carregando...')
    print()
    sleep(t)
    print(f'Bem vindo ao Jogo da velha do Tiede')
    print('-'*40)

    jg1 = str(input(f'Digite o nome do jogador 1 = '))
    jg2 = str(input(f'Digite o nome do jogador 2 = '))
    player = jg1
    letra = 'X'
    print('-'*40)

    # Printa o tabuleiro
    print(f'{tabuleiro[0]} | {tabuleiro[1]} | {tabuleiro[2]}')
    print(f'{tabuleiro[3]} | {tabuleiro[4]} | {tabuleiro[5]}')
    print(f'{tabuleiro[6]} | {tabuleiro[7]} | {tabuleiro[8]}')
    print()
    while cond:
        # Input da jogada
        p1 = int(input(f'{player}, escolha um numero! = '))
        p1 -= 1
        if tabuleiro[p1] in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
            tabuleiro[p1] = letra
        else:
            print(f'Numero escolhido, tente novamente!')
            continue

        print('-'*40)
        print(f'{tabuleiro[0]} | {tabuleiro[1]} | {tabuleiro[2]}')
        print(f'{tabuleiro[3]} | {tabuleiro[4]} | {tabuleiro[5]}')
        print(f'{tabuleiro[6]} | {tabuleiro[7]} | {tabuleiro[8]}')
        print('-'*40)

        # Troca o jogador
        if turno % 2 == 1:
            letra = 'O'
            player = jg2

        else:
            letra = 'X'
            player = jg1

        # Verifica as linhas
        l1 = tabuleiro[0] == tabuleiro[1] == tabuleiro[2] not in [
            '1', '2', '3', '4', '5', '6', '7', '8', '9']
        l2 = tabuleiro[3] == tabuleiro[4] == tabuleiro[5] not in [
            '1', '2', '3', '4', '5', '6', '7', '8', '9']
        l3 = tabuleiro[6] == tabuleiro[7] == tabuleiro[8] not in [
            '1', '2', '3', '4', '5', '6', '7', '8', '9']

        if l1 or l2 or l3:
            print(f'{player} Venceu')
            break

        # Verifica as colunas
        c1 = tabuleiro[0] == tabuleiro[3] == tabuleiro[6] not in [
            '1', '2', '3', '4', '5', '6', '7', '8', '9']
        c2 = tabuleiro[1] == tabuleiro[4] == tabuleiro[7] not in [
            '1', '2', '3', '4', '5', '6', '7', '8', '9']
        c3 = tabuleiro[2] == tabuleiro[5] == tabuleiro[8] not in [
            '1', '2', '3', '4', '5', '6', '7', '8', '9']
        
        if c1 or c2 or c3:
            print(f'{player} Venceu')
            break
        
        # Verifica as diagonais
        d1 = tabuleiro[2] == tabuleiro[4] == tabuleiro[6] not in [
            '1', '2', '3', '4', '5', '6', '7', '8', '9']
        d2 = tabuleiro[0] == tabuleiro[4] == tabuleiro[8] not in [
            '1', '2', '3', '4', '5', '6', '7', '8', '9']
        
        if d1 or d2:
            print(f'{player} Venceu')
            break
        
        # Verifica se teu empate
        cont = 0

        for i in tabuleiro:

            if i not in ['1','2','3','4','5','6','7','8','9']:
                cont += 1

            if cont == 9:
                print('Velha!')
        turno += 1
                

    replay = input('Deseja jogar novamente? [S/N] : ').upper()
    print('*'*200)