"""
Sum square difference
Problem 6

The sum of the squares of the first ten natural numbers is,
12 + 22 + ... + 102 = 385

The square of the sum of the first ten natural numbers is,
(1 + 2 + ... + 10)2 = 552 = 3025

Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

"""

def solve():
    square_of_sums = (101*50)**2  #sum(1..n) = n(n+1)/2 
    return square_of_sums - sum(n**2 for n in range(1,100))

if __name__=='__main__':
    print(solve())




