from random import randint
mat=[]
for i in range(5):
    mat.append([])
    for j in range(5):
        mat[i].append(randint(1,50))
        print("[{:2}] ".format(mat[i][j]),end='')
    print()

print("="*30)

print("Diagonal Principal")
for i in range(5):
    print("[{:2}] ".format(mat[i][i]),end='')

print("\n")
print("="*30)

print("Diagonal Principal")
for i in range(5):
    for j in range(5):
        if i==j:
            print("[{:2}] ".format(mat[i][j]),end='')
        else:
            print("[  ] ", end='')
    print()

            




