"""
Circular primes
Problem 35

The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.

There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

How many circular primes are there below one million?

"""

def number_to_digits(number):
    digits = []
    while number > 0:
        digits.insert(0, number % 10)
        number //= 10
    return digits

def digits_to_number(digits):
    exp = 0
    number = 0
    for i in reversed(digits):
        number += i*10**exp
        exp += 1
    return number

def rotations(digits):
    for i in range(len(digits)):
        yield digits[i:]+digits[:i]

def solve():
    N = [None,False] + [True]*999999             # mark all primes
    for i in range(1000001):
        if N[i]:
            N[i*2::i] = [False]*((len(N)-1-i) // i)
            
    count = 0
    for i,prime in enumerate(N):
        if prime:
            digits = number_to_digits(i) 
            if all(N[digits_to_number(perm)] for perm in rotations(digits)):
                count += 1
            
    return count

if __name__=='__main__':
    from time import time
    t1 = time()
    print('Found {} in {:.2f} miliseconds'.format(solve(),(time()-t1)*1000))
