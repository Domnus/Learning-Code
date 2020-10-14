#Bruno Campos - 610453
#Emmanuel Tiede RA: 569453
#Victor Rian RA: 600751
L = []

def insertion():
    print()
    color = str(input("Digite a cor desejada = "))
    hex_color = str(input("Digite o codigo da cor = "))
    L.append((color,hex_color))

def query():
    v = false
    print()
    color = input("Digite o nome da cor = ")
    for i in L:
        if i[0] == color:
            print(i[0])
            v = true
            break
    if not v:
        print("Cor não cadastrada")

def listing():
    print()
    print(L)
    print()

def menu():
    print("Menu:\n1 - Inserção\n2 - Consulta\n3 - Listagem\n4 - Sair")
    opc = int(input("Selecione uma opção -> "))
    return opc

while True:
    opc = menu()
    if opc == 1:
        insertion()
    elif opc == 2:
        query()
    elif opc == 3:
        listing()
    elif opc == 4:
        print("Obrigado por utilizar Cores em RGB")
        break
    else:
        print("Opção invalida")
        break