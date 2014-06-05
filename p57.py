"""
Square root convergents
Problem 57

It is possible to show that the square root of two can be expressed as an infinite continued fraction.

√ 2 = 1 + 1/(2 + 1/(2 + 1/(2 + ... ))) = 1.414213...

By expanding this for the first four iterations, we get:

    1 + 1/2 = 3/2 = 1.5
    1 + 1/(2 + 1/2) = 7/5 = 1.4
    1 + 1/(2 + 1/(2 + 1/2)) = 17/12 = 1.41666...
    1 + 1/(2 + 1/(2 + 1/(2 + 1/2))) = 41/29 = 1.41379...

    The next three expansions are 99/70, 239/169, and 577/408, but the eighth expansion, 1393/985, is the first example where the number of digits in the numerator exceeds the number of digits in the denominator.

    In the first one-thousand expansions, how many fractions contain a numerator with more digits than denominator?

"""
from lib.timer import best_time

def plus2AndInvert(n,d):
    return d,2*d + n

def add1(n,d):
    return n+d,d

def numGTdenom(n,d):
    return len(str(n)) > len(str(d))


def main():
    count = 0
    n,d = 1,2
    for _ in range(1000):
        if numGTdenom(*add1(n,d)): count += 1
        n,d = plus2AndInvert(n,d)

    return count


print(best_time(main))

