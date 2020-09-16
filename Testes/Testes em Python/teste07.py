def fib(n):
    i, j = 1, 0
    for k in range(1, n + 1):
        i, j = j, i + j
    return j


def fibRec(n):
    if n <= 2:
        return 1
    return fibRec(n-1) + fibRec(n-2)


numero = int(
    input("Informe o termo para ser exibido da sequencia de Fibonacci: "))
print("O {}º termo da sequencia de Fibonacci é {}".format(numero, fib(numero)))
print("O {}º termo da sequencia de Fibonacci é {}".format(numero, fibRec(numero)))
