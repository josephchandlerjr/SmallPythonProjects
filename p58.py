"""
Spiral primes
Problem 58

Starting with 1 and spiralling anticlockwise in the following way, a square spiral with side length 7 is formed.

37 36 35 34 33 32 31
38 17 16 15 14 13 30
39 18  5  4  3 12 29
40 19  6  1  2 11 28
41 20  7  8  9 10 27
42 21 22 23 24 25 26
43 44 45 46 47 48 49

It is interesting to note that the odd squares lie along the bottom right diagonal, but what is more interesting is that 8 out of the 13 numbers lying along both diagonals are prime; that is, a ratio of 8/13 ≈ 62%.

If one complete new layer is wrapped around the spiral above, a square spiral with side length 9 will be formed. If this process is continued, what is the side length of the square spiral for which the ratio of primes along both diagonals first falls below 10%?


The way to think of this is that you are building up squares. Since we are going clockwise the bottom corner is the last digit in the square.
Since we are starting at 1, and every layer's side increases by two from previous layer, each side length will be the next odd number. The
area of the square will be side**2 of course and that is also the bottom right most digit, which makes sense as the area of a square is the number
of units squared.

"""
from time import time

def get_corners(n,BR):
    ' n is side length'
    step = n-1
    return BR-step-step-step,BR-step-step,BR-step

def isprime(n):
    if n % 2 == 0: 
        return False
    for i in range(3,int(n**0.5)+1,2): #have eliminated even numbers, only examine odds
        if n % i == 0:
            return False
    return True

def main():
    PN = 0 # total prime numbers found on diagonals
    DN = 1 # diagonals numbers 
    side = 1 
    while True:
        side += 2
        BR = side*side
        corners = get_corners(side,BR)
        for c in corners:
            PN += isprime(c) # bool treated as 1 or 0 for this purpose
        DN += 4 
        if PN/DN < .1:
            return side 


t1 = time() 
print(main())
print(time()-t1)

