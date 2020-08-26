from functools import reduce
import time

def divisivel(a, b, x):
    if a % x == 0 or b % x == 0:
        return True
    return False

def encerrou(list):
    return reduce(lambda a, b: True if a == 1 or b == 1 else False, list)

def primo(num):
    if num == 1:
        return False
    for i in range(2, num//+1):
        if num % i == 0:
            return False
    return True

def MMC(*args):
    list = []
    div = []
    mmc = 1

    for i in range(len(args[0])):
        num = args[0][i]
        num = int(num)
        list.append(num)

    x = 2
    print(list)
    while not encerrou(list):
        if primo(x):
            for i in range(len(list)-1):
                if divisivel(list[i], list[i+1], x):
                    div.append(x)
                    for i in range(len(list)):
                        if list[i] % x == 0:
                            list[i] = list[i] // x
                    x = 2
                else:
                    x += 1

        print(list)
        print(div)
        time.sleep(3)

    for i in range(len(div)):
        mmc *= div[i]

    print(f"O MMC é {mmc}.")

MMC(input("Digite os números desejados separados por um espaço: ").split(" "))
