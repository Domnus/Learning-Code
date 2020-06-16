a = []

for i in range(7):
    a.append([])
    for j in range(7):
        a[i].append(0)
for i in range(7):
    for j in range(7):
        if i>=j:
            a[i][j]=i**2
        else:
            a[i][j]=j**2
for i in range(7):
    for j in range(7):
        print('[{:2}]'.format(a[i][j]), end=' ')
    print()



