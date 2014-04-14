#py10.py #
#The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
#
#Find the sum of all the primes below two million.


#using the Sieve of Eratosthenes
from lib.utils import prime_generator


if __name__ == '__main__':
    from time import time
    n = 2*10**6
    t1 = time()
    p = prime_generator(n)
    s = 0
    for x in p:
        s+=x
    print 'prime_generator found the sum of primes under'
    print '%s in %s seconds'%(n,(time()-t1))
    print 'the sum is %s' %s
