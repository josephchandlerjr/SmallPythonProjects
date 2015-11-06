"""
Summation of primes
Problem 10

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""

from lib.utils import prime_generator

def solve():
    n = 2*10**6
    p = prime_generator(n)
    s = 0
    for x in p:
        s+=x
    return s



if __name__ == '__main__':
    print(solve())
