#! /usr/bin/env python3
"""
Digit canceling fractions
Problem 33

The fraction 49/98 is a curious fraction, as an inexperienced mathematician in attempting to simplify it may incorrectly believe that 49/98 = 4/8, which is correct, is obtained by cancelling the 9s.

We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

There are exactly four non-trivial examples of this type of fraction, less than one in value, and containing two digits in the numerator and denominator.

If the product of these four fractions is given in its lowest common terms, find the value of the denominator.

"""

from fractions import Fraction

def cancel_digits(n,d):
    """
      a,b
      ---
      c,d
    """
    a,b,c,d = [ x for y in map(lambda x: (x // 10,x % 10), (n, d)) for x in y ]
    if a == c:
        return b,d
    elif a == d:
        return b,c
    elif b == c:
        return a,d
    elif b == d:
        return a,c
    else:
        return False


def main():
    numbers = list(range(10,100)) 
    result = Fraction(1)
    for i in range(len(numbers)):
        n,*rest = numbers[i:]
        for denominator in rest:
            if not all(x%10==0 for x in (n,denominator)):
                new = cancel_digits(n,denominator)
                if new and 0 not in new:
                    F = Fraction(n,denominator) 
                    newF = Fraction(*new)
                    if F == newF:
                        result *= F 
    
    return result
if __name__ == '__main__':
    print(main().denominator)
    

