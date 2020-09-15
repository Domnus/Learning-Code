def multmatriz(X, Y):
    c = [0] * len(X)
    for i in range(len(X)):
        c[i] = [0] * len(Y[0])
        for j in range(len(Y[0])):
            for k in range(len(Y)):
                c[i][j] += (X[i][k] * Y[k][j])
