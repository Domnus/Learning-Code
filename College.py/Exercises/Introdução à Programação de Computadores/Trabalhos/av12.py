print('=-' * 20)
print('            Jogo da Velha')
print('=-' * 20)

game_rodando = True
vencedor = None

player_atual = 'X'

tabuleiro = ['-', '-', '-', 
             '-', '-', '-', 
             '-', '-', '-']

def jogo():
    mostrar_tabuleiro()
    
    while game_rodando:
        turno()
            
        # game_parou():
            
        # trocar_player():
            

def mostrar_tabuleiro():
    print('\n')
    print(f"       {tabuleiro[0]} | {tabuleiro[1]} | {tabuleiro[2]}      1 | 2 | 3")
    print(f"       {tabuleiro[3]} | {tabuleiro[4]} | {tabuleiro[5]}      4 | 5 | 6")
    print(f"       {tabuleiro[6]} | {tabuleiro[7]} | {tabuleiro[8]}      7 | 8 | 9")
    print()


def turno():
    print(f'É a vez do {player_atual}!')
    
    while True:
        posicao = input('Escolha uma posição de 1 a 9-> ')
        if posicao not in ['1', '2', '3', '4' ,'5' ,'6' ,'7' ,'8' ,'9']:
            posicao = input('Escolha uma posição de 1 a 9-> ')
        else:
            posicao = int(posicao) -1
            if tabuleiro[posicao] != '-':
                print('Posição já ocupada! Escolha outra.')
            else:
                tabuleiro[posicao] = player_atual
        mostrar_tabuleiro()


jogo()