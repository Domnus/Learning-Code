num = int(input("Informe um número -> "))
print("\nA soma dos divisores de",num)
somaDiv = 0
for i in range(1,num//2+1):
    if num % i == 0:
        somaDiv += i
        if i < num//2:
            print("{} + ".format(i),end="")
        else:
            print("{} = ".format(i),end="")
print(somaDiv)