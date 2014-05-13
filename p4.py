#p4.py
# _*_ coding: UTF-8 _*_
#
#A palindromic number reads the same both ways. The largest palindrome 
#made from the product of two 2-digit numbers is 9009 = 91 × 99.
#
#Find the largest palindrome made from the product of two 3-digit numbers.


three_digit_numbers = range(100,1000)

def ispalindrome(n):
    if not n:
        return True
    else:
        n = str(n)
        if n[0] == n[-1]:
            return ispalindrome(n[1:-1])
        else:
            return False



print(max([x*y for x in three_digit_numbers for y in three_digit_numbers if x>=y if ispalindrome(x*y)]))



