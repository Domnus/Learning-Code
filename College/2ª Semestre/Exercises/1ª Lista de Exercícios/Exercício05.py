coca = input('Digite a frase dejesada: ')
f1 = list(coca)
f1.reverse()
acoc = ''.join(f1)

if coca == acoc:
    print("A frase é palíndrome")
else:
    print("A frase não é palíndrome")
