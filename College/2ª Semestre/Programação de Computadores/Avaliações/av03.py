# Bento Carlos Silva dos Santos RA: 600784
# Fernando Cremonez Costa RA: 604097

def menu():
    print("-----Criptografia-----")
    print("1. Criptografar")
    print("2. Descriptografar")
    print("3. Sair do Programa")

    return int(input("Escolha a opção-> "))

def criptografar():
    m = []
    n = []
    global lista
    frase = input("Digite a frase-> ")
    frase = list(frase)
    
    for i in range(len(frase)):
        if frase[i] in lista:
            j = lista.index(frase[i])
            m.append(j+1)
            
     for i in range()


while True:
    lista = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '.', '!', '#', ' ']
    global A = [3, 1, 2, 1]3

    global B = [1, -1, -2, 30]
    x = menu()
    if x == 1:
        print(f"Frase criptografada: \n{criptografar()}")
    elif x == 2:
        print(f"Frase descriptografada? \n{descriptografada()}")
    elif x == 3:
        break






