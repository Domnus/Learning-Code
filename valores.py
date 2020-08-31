valor = float(input("Digite o valor: "))

agualuz = valor * 0.11
iptu = valor * 0.0145
familia = valor * 0.05
fordka = valor * 0.2375
cetelem = valor  * 0.022
mercado = valor * 0.286
life_netflix_celular_amazon = valor * 0.06
outros = valor * 0.22

print("Água - Luz              |   11%| = {:.3f}".format(agualuz))
print("IPTU                    | 1.45%| = {:.3f}".format(iptu))
print("Família                 |    5%| = {:.3f}".format(familia))
print("Ford Ka                 |23.75%| = {:.3f}".format(fordka))
print("Cetelem                 | 2.20%| = {:.3f}".format(cetelem))
print("Mercado                 | 28.6%| = {:.3f}".format(mercado))
print("Life-Netflix-Celular-Amazon |6%| = {:.3f}".format(life_netflix_celular_amazon))
print("Outros                  |   22%| = {:.3f}".format(outros))
