"""
Smallest multiple
Problem 5

2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

"""


def solve():
    divisors =(11,12,13,14,15,16,17,18,19,20)
    n = 40
    while True:
        for i in divisors:
            if n % i != 0: 
                n += 20
                break
            if i == 20:
                return n

if __name__ == '__main__':
    print(solve())

