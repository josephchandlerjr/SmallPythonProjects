"""
Distinct primes factors
Problem 47

The first two consecutive numbers to have two distinct prime factors are:

    14 = 2 × 7
    15 = 3 × 5

    The first three consecutive numbers to have three distinct prime factors are:

    644 = 2² × 7 × 23
    645 = 3 × 5 × 43
    646 = 2 × 17 × 19.

    Find the first four consecutive integers to have four distinct prime factors. What is the first of these numbers?

"""

from time import time


def primes():
    """
    primes() 
    a generator that yields an indefinite number of primes
    """
    D = {}
    q = 2
    while True:
        if q not in D:
            D[q*q] = [q]
            yield q
        else:
            for p in D[q]:
                D.setdefault(q+p,[]).append(p)
        q+=1

def prime_factor_count(n):
    count = set()
    f = 2
    while n > 1: 
        while n % f == 0:
                count.add(f)
                n //= f
        f += 1
    return len(count)


def check_sequence(n):
    for i in range(n,n+4):
        if prime_factor_count(i) != 4:
            return False
    return True


def main():
    last_prime = 677 
    for prime in primes():
        count = 0
        for n in range(last_prime+1,prime-3):
            if check_sequence(n):
                    return n
        last_prime = prime


def solve():
    """
    cheating a bit and guessing at the upperbound but 
    much faster, even using 1million as upperbound and
    not 200k or something closer to actual result.
    """
    L = [None,None,0]+[0]*(1000000-2)
    count = 0
    for i in range(2,len(L)):
        if L[i] == 0:
            for j in range(i+i,len(L),i):
                L[j] += 1
        if L[i] != 4:
            count = 0
        else:
            count += 1
        if count == 4:
            return i-3

     
if __name__ == '__main__':
    t1 = time()
    print(solve())
    print (time()-t1)
