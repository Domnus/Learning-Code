from time import sleep
a = 0
cont = 0
while a<10:
    nome = input('Digite seu nome:' )
    a = float(input('Digite sua primeira nota: '))
    b = float(input('digite sua segunda nota: '))
    media = (a+b)/2
    if a<5:
        print('{} você está de recuperaçao, sua primeira nota é {} segunda é {} a media é {}'.format(nome,a,b,media))
    elif a>=5:
        print('{} você está aprovrado, sua primeira nota é {} segunda é {} a media é {}'.format(nome,a,b,media))
    elif a==10:
        print('{} parabéns, sua primeira nota é {} segunda é {} a media é {}'.format(nome,a,b,media))
    sleep(2)
print('Fim')