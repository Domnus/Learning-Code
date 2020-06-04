def myfunc(*args):
    even = []
    mylist = list(args)
    for number in mylist:
        if number % 2 == 0:
            even.append(number)
    print(even)
    
myfunc(5,6,7,8)
    

