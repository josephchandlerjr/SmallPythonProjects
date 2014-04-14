#p3.py
#
#The prime factors of 13195 are 5, 7, 13 and 29.
#What is the largest prime factor of the number 600851475143 ?

from lib.utils import factor, isprime

number = 600851475143 

if __name__=='__main__':
    print max(filter(isprime,factor(number)),key=lambda n: 0 if n==number else n) 
