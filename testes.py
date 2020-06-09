from random import randint
A = []
for i in range(5):
    A.append([])
    for j in range(5):
        A[i].append(randint(1,50))
        print("[{:2}]".format(A[i][j]),end=" ")
    print()

l = -1
for i in range(5):
    s = 0
    l+=1
    for j in range(5):
        s += A[i][j]
    print("A soma da linha {} é {} ".format(l,s))
