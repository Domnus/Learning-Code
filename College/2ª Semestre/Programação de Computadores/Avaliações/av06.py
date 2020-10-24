lista = []

for i in range(8):
    pessoa = input("")

    if pessoa in lista:
        lista.remove(pessoa)
    lista.insert(0, pessoa)

print(lista)
        
