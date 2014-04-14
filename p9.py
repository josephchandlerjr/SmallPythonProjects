#p9.py
#
#A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
#a^2 + b^2 = c^2
#
#For example, 3^2 + 4^2 = 9 + 16 = 25 = 52.
#
#There exists exactly one Pythagorean triplet for which a + b + c = 1000.
#Find the product abc.

from operator import mul

print next( ( reduce(mul, (a, b, c) ) ) 
        for a in range(1,1000)
        for b in range(2,1000)
        if a < b
        for c in range(3,1000) 
        if b < c
        if a + b + c == 1000
        if a**2 + b**2 == c**2 )
