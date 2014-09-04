"""
Lexicographic permutations
Problem 24

A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4. If all of the permutations are listed numerically or alphabetically, we call it lexicographic order. The lexicographic permutations of 0, 1 and 2 are:

    012   021   102   120   201   210

    What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?

"""

from math import factorial
from itertools import permutations
from time import time

statement = """There are 10! permutations of the numbers 0-9. If they are in lexicographic
               order than we can find out what number the millionth permutation begins with.
               for each starting digit there are 9! permutations. 9! = 362880. So there are
               362880 permutations starting with 0 and another 362880 beginning with 1 which
               equals 725760 permutations. Another addition of 9! would push the total over
               1 million and so the millionth lexicographic permutation must start with a 2""" 

place = 10**6


def first_digit():
    s = 0
    digit = None
    n = factorial(9)
    for x in range(10): 
        digit = x
        if s + n > 10**6:
            return s,digit
        else:
            s+=n

def solve():
    L = list(range(10))    
    index,start = first_digit()
    L.remove(start)
    res = (start,)+list(permutations(L))[place-index-1]
    return res


#print('Found {} in {:.2f} seconds'.format(res,t2-t1))


if __name__ == '__main__':
    print(solve())



