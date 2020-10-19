def has_33(list):
    for i in range(0, len(list)-1):
        if list[i:i+2] == [3,3]:
            return True
    return False

x = has_33([1,3,3])

print(f"Estado : {x}")
