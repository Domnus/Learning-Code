def fibonacci(n):
    if n <= 2:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)

n = int(input("Digite o enésimo dígito da sequência de Fibonacci -> "))
print(f"O enésimo será {fibonacci(n)}")