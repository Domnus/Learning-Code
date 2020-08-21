def has_33(list):
    for i in range(len(list)-1):
        if list[i:i+2] == [3,3]:
            return True
    return False

x = has_33([3,1,3])

print(x)
