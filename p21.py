# p21.py
# _*_ encoding: UTF-8  _*_
#
#amicable numbers
#Problem 21
#
#Let d(n) be defined as the sum of proper divisors of n 
#(numbers less than n which divide evenly into n).
#If d(a) = b and d(b) = a, where a ≠ b, then a and b are an 
#amicable pair and each of a and b are called amicable numbers.
#
#For example, the proper divisors of 220 are 
#1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. 
#The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.
#
#Evaluate the sum of all the amicable numbers under 10000.

from operator import add,mul
from lib.utils import isprime

def prime_divisors(n):
    prime_factors = {} 
    i = 2
    while i*i <= n:
        if n % i == 0:
            prime_factors[i] = 1
            n //= i
            while n % i == 0:
                n //= i
                prime_factors[i] += 1
        i += 1
    prime_factors[n] = 1
    return prime_factors

def sum_of_divisors():
    cache2 = {1:1}
    def _sum(n):
        try:
            return cache2[n]
        except KeyError:
            s = 0
            for i in range(1,n):
                if n % i == 0:
                    s += i
            cache2[n] = s
            return s
    return _sum

sum_of_divisors = sum_of_divisors()

def multiples(p):
    """
    takes a dictionary of prime divisors
    and their multiplicities and
    returns a list of divisors that are 
    multiples of that each
    """
    multiples = []
    for n in p.keys():
        m = []
        for i in range(0,res[n]+1):
            m.append(n**i)
        multiples.append(m) 
    return multiples 


def product(*args):
    """
    takes a list of list and returns a 
    list of combinations of those lists
    """
    res = [ []]
    pools = map(tuple,args)
    for pool in pools:
        res = [x+[y] for x in res for y in pool]
    for prod in res:
        yield tuple(prod)

def get_powers(m):
    biglist = []
    for k in m.keys():
        lst = []
        for i in range(0,m[k]+1):
            lst.append(k**i)
        biglist.append(lst)
    return biglist 

def sum_of_divisors1():
    cache = {1:1}
    def _sum(n):
        try:
            return cache[n]
        except KeyError:
            p_div = prime_divisors(n)
            powers = get_powers(p_div)
            prods = list(product(*powers))
            prods = set([x for x in [reduce(mul,p) for p in prods] if x != n]) 
            cache[n] = reduce(add,prods)
            return cache[n]
    return _sum

sum_of_divisors1 = sum_of_divisors1()

def are_amicable(*args):
    if sum_of_divisors(args[0]) != args[1]:
        return False
    if sum_of_divisors(args[1]) != args[0]:
        return False
    return True

def both_even_or_both_odd(n,m):
    if n % 2 == 0:
        return m % 2 == 0
    else:
        return m % 2 != 0

if __name__ == '__main__':
    from time import time
    def test1():
        print '{:<15} {:>20} {:>20}'.format('number','prime divisors', 'sum')
        for n in (220,284):
            p_div = prime_divisors(n)
            powers = get_powers(p_div)
            prods = list(product(*powers))
            print '{:<15} {:>20} {:>20}'.format(n,p_div,reduce(add,[reduce(mul,p) for p in prods]))
        if are_amicable(220,284):
            print 'they are amicable'
        s = 0
        t1 = time()
        for n in range(1,10000):
            for m in range(1,10000):
                if n > m:
                    if are_amicable(n,m):
                       print 'amicable numbers {} and {} found in {:f} seconds'.format(n,m,time()-t1)
                       s += (n+m)  
        print 'The sum of these amicable numbers is {}. Algorithm took {:f} seconds'.format(s,time()-t1)
   
    def test2():
        t1 = time()
        result = 0
        for n in range(1,10000):
            s = sum_of_divisors(n)
            if s > n and sum_of_divisors(s) == n:
                result += s+n
                print 'amicable numbers {} and {} found in {:f} seconds'.format(n,s,time()-t1)
        print 'The sum of these amicable numbers is {}. Algorithm took {:f} seconds'.format(result,time()-t1)
    test2()

