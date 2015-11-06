"""
Special Pythagorean triplet
Problem 9

A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
a^2 + b^2 = c^2

For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.

"""
from operator import mul

def solve():
     x = next( (a, b, c)   
            for a in range(1,1000)
            for b in range(2,1000)
            if a < b
            for c in range(3,1000) 
            if b < c
            if a + b + c == 1000
            if a**2 + b**2 == c**2 )
     return x[0] * x[1] * x[2]

if __name__ == '__main__':
    print(solve())
