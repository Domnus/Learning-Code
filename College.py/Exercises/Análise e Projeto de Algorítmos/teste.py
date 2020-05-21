v = 0
a = [0]*8
for i in range (8):
    a[i] = [0]*8
    for j in range (8):
        a[i][j] = v
        v = 1-v
    v = 1-v
for i in range (8):
    for j in range (8):
        print(a[i][j], end = "  ")
    print()