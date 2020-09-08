import numpy as np

def converte(mensa):
    novafrase = []
    for letra in mensa:
        novafrase.append(lista.index(letra))
    if len(novafrase) % 2 != 0 : #SE A FRASE É PAR OU IMPAR 
        novafrase.append(30) # SE FOR IMPAR NAO DA PRA DIVIDIR EM 2 PARTES.
    return novafrase

def converte2():
    global lista
    n2 = Descriptografar()
    frase = []
    for i in range(len(n2)):
        for j in range(len(n2[i])): #VAI PEGAR  A SEGUNDA LISTA
            frase.append(n2[i][j])
    
    for i in range(len(frase)):
        frase[i] = lista[frase[i]] #COMPARAR E CONVERTER COM A LISTA
    frase = ''.join(frase) #JUNTAR EM STR     
    return frase

def criptografar(mensa):
    global A
    m = converte(mensa)
    novafraseM = [[],[]]
    novafraseN = [[],[]]
    metade = len(m) // 2
    novafraseM[0] = m[:int(metade)] #  ':' == COMEÇO ATÉ A METADE
    novafraseM[1] = m[int(metade):] #  ':' == METADE ATÉ O FINAL
    novafraseN = np.dot(A,novafraseM)

    return novafraseN
    
def Descriptografar(): 
    global B
    n = input('Informe os numeros para conversão:')
    n = n.split(', ')
    for i in range(len(n)):
        n[i] = int(n[i])
    novafraseN = [[],[]]
    BN = [[],[]]
    metade = len(n) // 2
    novafraseN[0] = n[:int(metade)] #  ':' == COMEÇO ATÉ A METADE
    novafraseN[1] = n[int(metade):] #  ':' == METADE ATÉ O FINAL
    BN = np.dot(B,novafraseN) #MULTIPLICAR

    return BN
    
print('Opção 1 = Criptografar\nOpção 2 = Descriptografar\nOpção 3 = Sair Do programa\n')
while True:
    lista = "*ABCDEFGHIJKLMNOPQRSTUVWXYZ.!# "
    #lista = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '.', '!', '#', ' ']
    A = [[3,1],[2,1]]
    B = [[1,-1], [-2,3]]
    opção = int(input('Informe a opção:'))
    if opção == 1:
        mensagem = input("Informe a mensagem:").upper().replace(' ','#')
        listaNum = criptografar(mensagem)
        for i in range(len(listaNum)):
            for j in range(len(listaNum[i])):
                print(f'{listaNum[i][j]}', end=', ')
        print()
    if opção == 2:
        NumInLetra = converte2()
        print(NumInLetra)
    if opção == 3:
        break

