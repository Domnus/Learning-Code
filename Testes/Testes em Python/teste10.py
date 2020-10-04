def sumall(*args):
    return sum(args[0])

values = list(map(int, input("Digite os valores: ").split()))

print(f"A soma dos valores é {sumall(values)}")