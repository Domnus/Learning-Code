from functools import reduce    # need this line if you're using Python3.x

def lcm(a, b):
    if a > b:
        greater = a
    else:
        greater = b

    while True:
        if greater % a == 0 and greater % b == 0:
            lcm = greater
            break
        greater += 1

    return lcm

def get_lcm_for(your_list):
    return reduce(lambda x, y: lcm(x, y), your_list)

def make_list(*args):
    list = []

    for i in range(len(args[0])):
        num = args[0][i]
        num = int(num)
        list.append(num)

    return list

list = make_list(input("Digite número separados por um espaço: ").split(" "))
ans = get_lcm_for(list)
print(ans)
