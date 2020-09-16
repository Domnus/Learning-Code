def fatorial(num):
    fat = 1
    for i in range(1, num+1):
        fat *= i
    return fat


def fatRec(num):
    if num == 1:
        return num
    return num * fatRec(num - 1)


numero = int(input("Informe um número para calcular o fatorial: "))
print("O fatorial de {} é {}".format(numero, fatorial(numero)))
print("O fatorial de {} é {}".format(numero, fatRec(numero)))
