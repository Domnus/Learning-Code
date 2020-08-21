def primo_Ou_Nao(num):
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

x = int(input("Digite um número: "))

if x:
    print("Número primo")
else:
    print("Não é primo")
