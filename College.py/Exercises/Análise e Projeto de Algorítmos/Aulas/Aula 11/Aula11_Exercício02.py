a = 0
b = 1
c = 1
A= []
print('-----20 primeiros números da série de Fibonacci-----')
for i in range(20):
    A.append(c)
    c = a + b
    a = b
    b = c
   
print(A)