from functools import reduce
import time

def divisivel(a, b, x):
    if a % x == 0 or b % x == 0:
        return True
    return False

def encerrou(list):
    return reduce(lambda a, b: True if a == 1 or b == 1 else False, list)

def primo(num):
    # If given number is greater than 1
    if num > 1:

       # Iterate from 2 to n / 2
       for i in range(2, num):

           # 2 and n / 2, it is not prime
           # If num is divisible by any number between
           if (num % i) == 0:
               return False
               break
       else:
           return True

    else:
       return False

def MMC(*args):
    list = []
    div = []
    mmc = 1

    for i in range(len(args[0])):
        num = args[0][i]
        num = int(num)
        list.append(num)

    x = 2

    while not encerrou(list):
        if primo(x):
            c = reduce(lambda a,b: divisivel(a, b, x), list)
            if c:
                div.append(x)
                for i in range(len(list)):
                    if list[i] % x == 0:
                        list[i] = list[i] / x
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
