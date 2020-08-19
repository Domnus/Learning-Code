from random import randint

list = [0] * 10

for i in range(10):
    list[i] = [0] * 10
    for j in range(10):
        list[i][j] = randint(1, 50)

for i in range(10):
    for j in range(10):
        print(f"[{list[i][j]}]", end='')
    print()

def maiorColuna(coluna):
    for i in range(len(list)):
        for j in list[coluna][i]:
            if i > maior:
                maior = i
    return maior

print(maiorColuna(3))
