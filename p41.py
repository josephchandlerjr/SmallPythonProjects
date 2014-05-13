"""
Pandigital prime
Problem 41

We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital and is also prime.

What is the largest n-digit pandigital prime that exists?

"""

from lib.utils3 import decrement_pandigital
from math import ceil

def prime_list(stop):
    p = [False,False]+[True]*(stop-1)
    for i in range(int(stop**0.5)+1):
        if p[i]:
            p[i+i::i] =[False]*((len(p)-1-i) // i)
    return p

def digits_to_number(n):
    number = 0
    i = len(n)-1
    for digit in n:
       number += digit*10**i
       i-=1
    return number

def is_prime(n):
    for i in range(2,int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def get_all_n_pan_numbers():
    pandigitals = []
    for n in range(2,10):
        low  = digits_to_number(range(1,n+1))
        high = digits_to_number( list(reversed(range(1,n+1)))    )
        pandigitals.append((high,low))
    return pandigitals


def main():
    pandigitals = get_all_n_pan_numbers()
    for (high,low) in reversed(pandigitals):
        while True:
            if is_prime(high):
                return high
            if high == low:
                break
            high = int(decrement_pandigital(high))

if __name__=='__main__':
    from lib.timer import best_time
    print(best_time(main))

