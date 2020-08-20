def primoOuNao(num):
    # If given number is greater than 1
    if num > 1:

       # Iterate from 2 to n / 2
       for i in range(2, num):

           # If num is divisible by any number between
           # 2 and n / 2, it is not prime
           if (num % i) == 0:
               return False
               break
       else:
           return True

    else:
       return False

num = int(input("Digite um número: "))
if primoOuNao(num):
    print("Número Primo.")
else:
    print("Não primo.")
