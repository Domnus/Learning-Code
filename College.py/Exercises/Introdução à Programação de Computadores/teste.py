import random
cont = 0
cond = True
cond2 = True
while cond:
    x = random.randint(100, 1000)
    c = x // 100
    d = (x % 100) // 10
    u = x % 10
    if c != d and c!= u and d != u:
        cond = False
    else:
        cond = True
while cond2:
    c = x // 100
    d = (x % 100) // 10
    u = x % 10
    if c > d and c > u:
      if d > u:
            menor = (u*100) + (d * 10) + c
            maior = (c * 100) + (d * 10) + u
      else:
            menor = (d * 100) + (u * 10) + c
            maior = (c * 100) + (u * 10) + d
    elif d > c and d > u:
      if c > u:
            menor = (u*100) + (c * 10) + d
            maior = (d * 100) + (c * 10) + u
      else:
            menor = (u * 100) + (c * 10) + d
            maior = (d * 100) + (u * 10) + c
    elif u > c and u > d:
      if c > d:
            menor = (d*100) + (c * 10) + u
            maior = (u * 100) + (c * 10) + d
      else:
            menor = (c * 100) + (d * 10) + u
            maior = (u * 100) + (d * 10) + c
    x = maior - menor
    cont += 1
    cond2 = x != 495

print("Total de iterações : {}".format(cont))

        



        

