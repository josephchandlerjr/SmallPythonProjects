# p20.py
# _*_ encoding: UTF-8  _*_
#factorial digit sum
#Problem 20
#
#n! means n × (n − 1) × ... × 3 × 2 × 1
#
#For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
#and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.
#
#Find the sum of the digits in the number 100!


from math import factorial

n = factorial(100)
res = sum([int(x) for x in str(n)])
print 'the sum of the digtis in the number 100! is {}'.format(res)
