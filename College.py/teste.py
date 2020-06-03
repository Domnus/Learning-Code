from random import randint

print("","=-" * 20, "\n           * IMAGEM BITMAP *\n", "=-" * 20, "\nOpções: 1-Criar Matriz; 2-Compactar Imagem; 3-Descompactar Imagem; 4-Sair do Programa")
op = int(input("Selecione uma opção: "))
while (op != 1 and op != 2 and op != 3 and op != 4):
    op = int(input("NÚMERO INVÁLIDO! Digite um número entre 1 e 4: "))

while op != 4:

    if(op == 1):
        resp = input("Criar a matriz manualmente (M) ou randomicamente (R): ").upper()[0]
        while (resp != "M" and resp != "R"):
            resp = int("Resposta Inválida! Digite M ou R: ")
        l = int(input("Digite o número de linhas da matriz: "))
        c = int(input("Digite o número de colunas da matriz: "))
        matriz = [0] * l
        VetCompact = []
        cont = -1
        if (resp == "M"):
            print("\nCrie a Imagem:")
            for i in range(l):
                matriz[i] = [0] * c
                for j in range(c):
                    matriz[i][j] = int(input(f"Digite o valor (0 ou 1) da posição {i + 1}x{j + 1}: "))
                    while (matriz[i][j] != 0 and matriz[i][j] != 1):
                        matriz[i][j] = int(input(f"VALOR INVÁLIDO! Digite 0 ou 1 para a posição {i + 1}x{j + 1}: "))
            print("\n\nAqui está a imagem que você criou:")
        else:
            for i in range (l):
                matriz[i] = [0]*c
                for j in range (c):
                    matriz[i][j] = randint(0,1)
            print("\nAqui está a imagem criada randomicamente:")
        for i in range(l):
            for j in range(c):
                if matriz[i][j] == 1:
                    print("\033[0:33:47m   \033[m", end="")  # 'pixel' CINZA
                else:
                    print("\033[0:33:40m   \033[m", end="")  # 'pixel' BRANCO
            print()

    if (op == 2):                                                                                                           # 2 = COMPACTAR IMAGEM
        vetCompact = []
        cont = -1
        resp = input("\nUtilizar uma imagem pronta (P) ou Criar imagem manualmente (M): ").upper()[0]
        if (resp == "M"):
            l = int(input("Digite o número de linhas da matriz: "))
            c = int(input("Digite o número de colunas da matriz: "))
            matriz = [0]*l
            for i in range(l):
                matriz[i] = [0] * c
                for j in range(c):
                    matriz[i][j] = int(input(f"Digite o valor (0 ou 1) da posição {i + 1}x{j + 1}: "))
                    while (matriz[i][j] != 0 and matriz[i][j] != 1):
                        matriz[i][j] = int(input(f"VALOR INVÁLIDO! Digite 0 ou 1 para a posição {i + 1}x{j + 1}: "))

        print(f"\nImagem Compactada: ", end="")
        for i in range(l):
            p, b = 0, 0
            for j in range(c):
                if (matriz[i][j] == 1):
                    p += 1
                if (matriz[i][j] == 0):
                    b += 1
                if j == c - 1 or matriz[i][j] != matriz[i][j + 1]:
                    if (p > 0):
                        vetCompact.append(f"{p}P")
                        print(f"{p}P", end="")
                        cont += 1
                    elif (b > 0):
                        vetCompact.append(f"{b}B")
                        print(f"{b}B", end="")
                        cont += 1
                    p, b = 0, 0
            vetCompact.append(0)
            print("0", end="")
            cont += 1
        vetCompact.append(0)
        print("0")
        cont += 1


    if (op == 3):
        compac = input("Digite (ou cole) aqui a imagem compactada (apenas preto e branco): ")
        print("\nImagem descompactada: ")

        for i in range (len(compac)):
            if (compac[i] == '0'):
                print()
            elif (compac[i].isnumeric()):
                n = int(compac[i])
            elif (compac[i] == "P"):
                print("1  "*n, end = "")            # Obs: print("\033[0:33:47m \033[m" * n, end="") PARA BIT CINZA
            elif (compac[i] == "B"):
                print("0  "*n, end = "")            # Obs: print("\033[0:33:40m \033[m" * n, end="") PARA BIT BRANCO

    op = int(input("\nSelecione uma das opções: 1-Criar Matriz; 2-Compactar Imagem; 3-Descompactar Imagem; 4-Sair do Programa: "))

x = input("\nPrograma Encerrado\nPressione qualquer tecla para fechar a janela.")