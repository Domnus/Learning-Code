a = 0
b = 1
c = 1
A= []

for i in range(20):
    A.append(c)
    c = a + b
    a = b
    b = c
   
print(A)