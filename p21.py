"""
Amicable Numbers
Problem 21

Let d(n) be defined as the sum of proper divisors of n 
(numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an 
amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 
1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. 
The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
"""


def sum_of_divisors(n,cache={1:1}):
    try:
        return cache[n]
    except KeyError:
        s = 0
        for i in range(1,n):
            if n % i == 0:
                s += i
        cache[n] = s
        return s

def solve():
    result = 0
    for n in range(1,10000):
        s = sum_of_divisors(n)
        if s > n and sum_of_divisors(s) == n:
            result += s+n
    return result


if __name__ == '__main__':
    print(solve())
   
