def almost_there(num):
    if num  <= 110 and num >= 90 or num <= 210 and num >= 190:
        return True
    else:
        return False

x = almost_there(209)

print(x)
