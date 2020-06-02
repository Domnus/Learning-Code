desafio = True
arr = []
while desafio:
    imagem = []
    p = 0
    b = 0
    print('------Menu------')
    print('1 – Inserir a imagem (criar a matriz (max. 20x20) \n2 – Compactar a imagem \n3 – Descompactar a imagem \n4 – Sair do programa')
    inp = int(input('-> '))
    if inp == 1:
        h, w = input('Digite o tamanho da imagem [HxW] -> ').split('x')
        h = int(h)
        w = int(w)
        if h > 20 or w > 20:
            print('A matriz não deve ultrapassar 20x20')
        else:
            print('Digite os valores da matriz:')
            arr = [0] * h
            for i in range(h):
                arr[i] = [0] * w
                cond = 0
                while cond < w:
                    x = int(input(f'[{i}x{cond}] -> '))
                    if x != 0 and x != 1:
                        print('Digite apenas 1 ou 0!')
                    else:
                        arr[i][cond] = x
                        cond += 1
                
        for i in range(h):
            for j in range(w):
                print(f'[{arr[i][j]}]', end='')
            print()
    elif inp == 2:
        if not arr:
            print('=' * 39)
            print('=Primeiro digite os valores da matriz!=')
            print('=' * 39)
            continue
        else:
            for i in range(h):
                for j in range(w):
                    if arr[i][j] == 0:
                        b += 1
                    else: 
                        p += 1
    elif inp == 3:
        print('Digite o vetor da imagem compactada:')            
        imagem_compactada = input('-> ')
        for character in imagem_compactada:
            try:
                imagem.append(int(character))
            except ValueError:
                pass
        print(imagem)
