"""
Power digit sum
Problem 16

215 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 21000?
"""

def solve():
    return sum([int(n) for n in str(2**1000)])

if __name__ == '__main__':
    print(solve())
