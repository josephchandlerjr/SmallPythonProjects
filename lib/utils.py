#utils.py
from time import time

def factor(n):
    """ 
    factor(n)
    Returns set of factors for a given int"
    """
    if n == 0:
        return 0
    factors = [(i,n//i) for i in range(1,int(n**0.5)+1) if n%i == 0]
    res = set()
    for fact1, fact2 in factors:
        res.add(fact1); res.add(fact2)
    return res

def isprime(n):
    """
    def isprime(n)
    Returns True if n is prime else False"
    """
    if n < 2:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i == 0:
            return False
    return True

def timer(f):
    """
    timer(f)
    decorator
    reports time taken to complete function f
    """

    def _f(*args):
        t1 = time()
        res = f(*args)
        time_elapsed = time()-t1
        print('%s completed in time %f' %(f.__name__, time_elapsed))
        return res 
    return _f

def prime_generator(stop=100):
    """
    prime_generator(stop)
    Generator of primes up to but not including the
    value of `stop`
    stop must be an integer > 2 
    Uses Sieve of Eratosthenes.
    """
    numbers = [False]*2 + [True]*(stop-2)
    for i,val in enumerate(numbers):
        if val is True:
            if i < stop**0.5+1:
                numbers[i*2::i] = [False] * ((stop-1)/i - 1) 
            yield i

def prime_factors(n):
    """
    prime_factors(n):
    Returns list of prime factors. 
    Each factor occurs in this list
    as many times as is its multiplicity.
    """
    primes = []
    p = 2
    while p*p <= n:
        while n % p == 0:
            primes.append(p)
            n //= p
        p += 1
    if n > 1:
        primes.append(n)
    return primes

def number_of_factors(n):
    """
    number_of_factors(n)
    Returns the number of factors of n
    """
    if n == 1:
        return 0
    m = [] 
    p = 2
    while p*p <= n:
        count = 0
        while n % p == 0:
            count += 1
            n /= p
        if count > 0:
            m.append(count) 
        p +=1
    if n > 1:
        if n == p:
            m[-1] += 1
        else:
            m.append(1)
    res = 1 
    for n in m:
        res *= n+1

    return res


def multiplicity(p,n):
    """
    find_multiplicity(p,n)
    Returns the multiplicty of p, as a factor of n
    """
    i = 0
    while n % p**(i+1) == 0 :
        i += 1   
    return i

def number_of_factors1(n):
    """
    number_of_factors(n)
    Returns the number of factors of n including n itself
    """
    res = 1
    primes = prime_factors_multiplicities(n)
    for p in primes:
        res *= p+1
    return res

def memoizer(f):
    cache = {}
    def _f(*args):
        if args in cache.keys():
            return cache[args]
        else:
            cache[args] = f(*args)
            return cache[args] 

    return _f

def decrement_pandigital(n):
    string = str(n)  
    to_swap = 0
    for i in range(len(string)-1,0,-1):
        if string[i-1] > string[i] and string[i-1] != '1':
            to_swap = i-1
            break
    msd = string[:to_swap]
    lsd = "".join(reversed(sorted(string[to_swap+1:])))
    digit = string[to_swap]
    for other_digit in lsd:
        if digit > other_digit:
            digit,lsd = other_digit, lsd.replace(other_digit,digit)
            break                
    return  msd+digit+lsd

    
if __name__ == '__main__':   
    from primes import primes
    from composites import composites
    
    @timer
    def test():
        assert all(map(isprime,primes))
        assert not any(map(isprime,composites))
    test()
             
