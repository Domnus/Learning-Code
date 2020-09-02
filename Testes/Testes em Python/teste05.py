from time import sleep 

num = int(input("Digite uma frase: "))
x = num
while x > 0:
    x //= 10
    print(x)
    sleep(1)