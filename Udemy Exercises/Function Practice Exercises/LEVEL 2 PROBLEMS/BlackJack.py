def blackjack(a, b, c):
    sum = a + b + c

    if sum <= 21:
        return sum
    if sum > 21: 
        if a == 11 or b == 11 or c == 11:
            return sum  - 10
        return 'BURST'

print(blackjack(9,9,11))
