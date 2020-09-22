# Alisson Juan Feitoza RA: 601081
# Bento Carlos Silva dos Santos RA: 600784
# Fernando Cremonez Costa RA: 604097

def soma(A):
    try:
        if A < 1:
            A*= 1
        else:
            A / 10
        
        for i in range(len(A)-1):
            return soma(A[i]) + soma(A[i+1])
    except:
        Exception

A = [int(x) for x in input("Digite os números: ").split()]

print(f"A soma dos primeiros dígitos é {soma(A)}")
