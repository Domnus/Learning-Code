n = int(input())   

n = 12663989 / 983

print(n)


for i in range(1, n/2):
    if n % i == 0:
        print(n)    
        break
    
