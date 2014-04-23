#! /usr/bin/env python3
# _*_ encoding: UTF-8  _*_
"""
#Reciprocal cycles
#Problem 26
#
#A unit fraction contains 1 in the numerator. The decimal representation of the unit fractions with denominators 2 to 10 are given:
#
#1/2 =   0.5
#1/3 =   0.(3)
#1/4 =   0.25
#1/5 =   0.2
#1/6 =   0.1(6)
#1/7 =   0.(142857)
#1/8 =   0.125
#1/9 =   0.(1)
#1/10    =   0.1
#
#Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be seen that 1/7 has a 6-digit recurring cycle.
#
#Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.
"""

def find_period(d):
    """ 
    Essentially emulates long division keeping track of remainders.
    If remainder becomes zero, return None as decimal terminates.
    if remainder is periodic, return length of period
    """
    remainders = []
    rem = 1
    while rem > 0:
        while rem < d:
            rem *= 10
        rem = rem % d
        if rem in remainders:
            return len(remainders) - remainders.index(rem) 
        remainders.append(rem)
    return None    

def main():
    longest = (0,0)
    for d in range(1000,-1,-1):
        p = find_period(d)
        if p:
            longest = p  > longest[0] and (p,d) or longest
        if longest[0] > d-1:
            break #period of 1/d is is upper bounded by d-1
    return longest 

if __name__=='__main__':
   from time import time
   t1 = time()
   result = main() 
   t2 = time()
   print('Longest recurring cycle is of length {1} with denominator {2}. Found in {0:.2f}'.format(t2-t1,*result))



