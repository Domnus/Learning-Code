def verificaPrimo(num):
    if num == 1:
        return False
    for i in range(2, num//+1):
        if num % i == 0:
            return False
    return True


print(verificaPrimo(int(input("-> "))))