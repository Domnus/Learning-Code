def quadrados(n):
    return list(x*x for x in range(1,n+1))

n = int(input("Digite um número: "))
print(f"{n} primeiros quadrados perfeitos: ", end="")
print(*quadrados(n))
        
