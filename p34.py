"""
Digit factorials
Problem 34

145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial of their digits.

Note: as 1! = 1 and 2! = 2 are not sums they are not included.

"""

# upper bound:
# let d = number of digits on each side of the equation
# the largest value on each side of are
# 10^d -1 = d * 9!
# upperbound is 7 digits long
# 7*9! = 2540160 so that could be an upper bound
# but also 1! + 6 * 9! = 2177280 so so 1999999 > sum of it's factorials
# which is not a factorion but you can see that we've entered the realm of number > sum of factorial of digits
# the next highest sum of factorialis is 1999998 = 1854721 
# lets use 1854721 as our upper bound

from math import factorial as f

upper_bound = 1857421
factorials = {n:f(n) for n in range(10)}

def sum_of_factorials(n,cache={}):
    string = str(n) 
    length = len(string)
    h = tuple(sorted(string))
    try:
        return cache[h]
    except KeyError:
        total = 0
        if n == 40584: print(n)
        while n > 0:
            if n == 40584: print(n)
            x = n % 10
            total += factorials[x]
            n = n//10
        cache[h] = total
        return total

def solve():
    result = 0
    for n in range(3,upper_bound+1):
        if sum_of_factorials(n) == n:
            result += n 
    return result 

if __name__=='__main__':
    from time import time
    t1 = time()
    print('Found {} in {:.2f} seconds.'.format(solve(),time()-t1))
