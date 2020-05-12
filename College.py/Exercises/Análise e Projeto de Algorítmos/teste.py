a = [0]*5
print ("Digite os numeros da matriz:  ")
for i in range (5):
    a[i] = [0]*5
    for j in range (5):
        a[i][j] = int(input())
    
for i in range (5):
    soma = 0
    for j in range (5):
        soma += a[i][j]
    print (soma)
            




