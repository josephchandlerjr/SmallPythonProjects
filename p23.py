'''
non-abundant sums
Problem 23

A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example,
the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant numbers 
is 24. By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers.
However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be 
expressed as the sum of two abundant numbers is less than this limit.

Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
'''
from math import ceil
from time import time

def is_abundant(n):
    mid = ceil(n**0.5)
    s = 1+sum([(i+n//i) for i in range(2,ceil(n**0.5)) if n % i == 0])
    if mid == n**0.5: 
        s += mid
    return s > n

def get_abundants(limit):
    return [n for n in range(12,limit+1) if is_abundant(n)]

def sum_non_abn(limit):
    abundant_numbers = get_abundants(limit)
    L = {x+y for x in abundant_numbers for y in abundant_numbers if x >= y}
    return sum(n for n in range(limit+1) if n not in L)


def solve():
    limit = 28123 
    return sum_non_abn(limit)


if __name__=='__main__':
    print(solve())
