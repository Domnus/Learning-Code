# LESSER OF TWO EVENS: Write a function that returns the lesser 
# of two given numbers if both numbers are even, but returns the 
# greater if one or both numbers are odd

def lesser_of_two_evens(x, y):
    if x % 2 == 0 and y % 2 == 0:
        if x < y:
            print(x) 
        else:
            print(y)
    else:
        if x > y:
            print(x)
        else:
            print(y)

lesser_of_two_evens(2,5)
