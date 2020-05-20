user='fernando'
password='12345'
contador=3

while contador > 0:
    usuario=str(input('Usuário:'))
    senha=str(input('Senha:'))
    if usuario==user and senha==password:
        print('Acesso permitido, bem-vindo!')
        break
    else:
        print('Acesso negado! Usuário e/ou senha incorretos')
        contador-=1
        print('Restam', contador, 'chance(s)')