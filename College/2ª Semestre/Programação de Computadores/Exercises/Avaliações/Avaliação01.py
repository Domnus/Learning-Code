# Bento Carlos Silva dos Santos RA: 600784
# Fernando Cremonez Costa RA: 604097

coca = input("Mensagem codificada: ").upper()

coca = list(coca)

for i in range(len(coca)):
    try:
        if "P" == coca[i+1]:
            continue
    except:
        Exception
    else:
        coca.pop(i)
        
coca = "".join(coca)
print(coca)

 