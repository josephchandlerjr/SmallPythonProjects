"""
Double-base palindromes
Problem 36

The decimal number, 585 = 10010010012 (binary), is palindromic in both bases.

Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.

(Please note that the palindromic number, in either base, may not include leading zeros.)

"""

def is_palindrome(string):
    if len(string) < 2:
        return True
    if string[0] != string[-1]:
        return False
    return is_palindrome(string[1:-1])

def mybin():
    tmp = bin
    def f(n):
        return tmp(n)[2:]
    return f
bin = mybin()
total = 0
for n in range(1000001):
    if all(map(is_palindrome,(str(n),bin(n)))):
        total += n
print(total)
