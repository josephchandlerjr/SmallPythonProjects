#! /usr/bin/env python3
"""
Pandigital products
Problem 32

We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once; for example, the 5-digit number, 15234, is 1 through 5 pandigital.

The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing multiplicand, multiplier, and product is 1 through 9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.
HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.
"""

from itertools import permutations

# let r, m , p = number of digits in multiplier, multiplicand , produce respectively
# 1 <=  r <= m <= p <= 9
# m + r + p = 9
# p cannot be 3 or less ,  even the 100*100 yeilds a 4 digit number 
# p cannot be >= 5 or because even 99*99 does not yield a 5 digit number 
# so p == 4
# possible patterns given 9 digits are
#
#       multiplicand    multiplier   product
#         digits        digits        digits
#           1               4           4
#           2               3           4 
#
#   so multiplicand must have < 3 digits and multiplier must have < 5 digits

def is_pan(n):
    nums = set(n)
    return nums == is_pan.match

is_pan.match = set('123456789')

def inner(m,visited=[]):
    for r in range(2,99):
        p = m * r
        if p in visited:
            continue
        string = str(m)+str(r)+str(p)
        L = len(string)
        if L != 9:
            if L > 9:
                return
        elif is_pan(string):
            yield p
            visited.append(p)

def outer():
    return sum(product for m in range(123,9877) for product in inner(m))


def main2():
    return outer()

if __name__ == '__main__':
    from time import time
    t1=time()
    print(main2())
    print(time()-t1)
    
