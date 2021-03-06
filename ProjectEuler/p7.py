"""
10001st prime
Problem 7

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?

"""
from lib.utils import prime_generator

def solve():
    p = prime_generator(2000000)
    count = 0
    for n in p:
        count+=1
        if count == 10001:
            return n
 

if __name__=='__main__':
    print(solve())

        
