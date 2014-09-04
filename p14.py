"""
Longest Collatz sequence
Problem 14

The following iterative sequence is defined for the set of positive integers:

    n → n/2 (n is even)
    n → 3n + 1 (n is odd)

    Using the rule above and starting with 13, we generate the following sequence:
        13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1

        It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been 
        proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

        Which starting number, under one million, produces the longest chain?

        NOTE: Once the chain starts the terms are allowed to go above one million.

"""
from lib.utils import memoizer

def collatz(n):
    """
    collatz(n)
    Returns next collatz number in chain
    """
    if n % 2 == 0:
        return n>>1
    else:
        return 3*n+1

def collatz_chain_length_calculator():
    """
    collatz_chain_length_calculator()
    Returns a function which c
    """
    cache = {}
    def f(x):
        count = 0
        n = x
        while n > 1:
            count += 1 
            if n in cache:
                count += cache[n]
                break
            n = collatz(n)
        cache[x] = count
        return count
    return f

def solve():
        collatz_chain_length = collatz_chain_length_calculator()
        longest = (0,0)
        for x in range(10**6):
            l = collatz_chain_length(x)
            if l > longest[1]:
                longest = (x,l)
        return longest[0]

if __name__ == '__main__':
    print(solve())
