def acimaMedia(valor,media):
    if valor > media:
        return True
    return False

values = list(map(float, input('Digite os valores desejados: ').split(' ')))

print(f"Quantidade de valores lidos: {len(values)}.")

print(f"Valores lidos: ", end='')

[print(x,end=' ') for x in values]
print()

print(f"Soma dos valores: {sum(values)}.")

media = sum(values)/len(values)
print(f"Média dos valores: {media}.")

print(f"Valores acima da média: {list(filter(lambda x: x > media, values))}.")

print(f"Valores menores que 7: {[x for x in values if x < 7]}.")
