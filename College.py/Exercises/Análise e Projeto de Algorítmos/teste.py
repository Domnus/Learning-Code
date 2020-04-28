a = 0
b = 0
c = 0
cond = True
while cond:
    player1 = int(input('Digite um valor '))
    player2 = int(input('Digite um valor '))
    player3 = int(input('Digite um valor '))
    if player1 != player2 and player1!=player3:
        a+=1
    if player2!=player1 and player2!=player3:
        b+=1
    if player3!=player1 and player3!=player2:
        c+=1
    if a == 3:
        print('O jogador A é o vencedor!')
        cond = False
    if b == 3:
        print('O jogador B é o vencedor!')
        cond = False
    if c == 3:
        print('O jogador C é o vencedor!')
        cond = False

        