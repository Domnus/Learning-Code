tradutor = {'autismo': 'autism', 'autism': 'autismo'}


def buscar(palavra):
    if palavra not in tradutor:
        return "Palavra inválida"
    return tradutor[palavra]

while True:
    x = input("Digite uma palavra para tradução: ")
    print(buscar(x))
