"""

Goldbach's other conjecture
Problem 46

It was proposed by Christian Goldbach that every odd composite number can be written as the sum of a prime and twice a square.

9 = 7 + 2×1^2
15 = 7 + 2×2^2
21 = 3 + 2×3^2
25 = 7 + 2×3^2
27 = 19 + 2×2^2
33 = 31 + 2×1^2

It turns out that the conjecture was false.

What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?

"""

def prime_generator():
    """
    prime generator

    """
    D = {}
    q = 2
    while True:
        if q not in D:
            yield q
            D[q*q] = [q] # not next muliple without duplicating a multiple we would be already tracking
        else:
            for p in D[q]:
                D.setdefault(p+q, []).append(p)   # next multiple of each p starting at q

            del D[q]
        q += 1

def prime_plus_twice_square(p,sqr,cache={}):
    try:
        sqr = cache[sqr]
    except KeyError:
        cache[sqr] = sqr = sqr**2
    finally:
        return p + sqr + sqr 

def find_sqr(odd,p,cache={}):
    sqr = 0 
    res = prime_plus_twice_square(p,1)
    while res < odd:
        sqr += 1
        try:
            res = cache[(p,sqr)]
        except KeyError:
            res = cache[(p,sqr)] = prime_plus_twice_square(p,sqr)
    return res == odd    


def search_primes(odd,prime_list):
    for p in prime_list[:-1]:   
        if find_sqr(odd,p):
            return True
    return False


def main():
    prime = prime_generator() 
    prime_list = []
    prime_list.append(next(prime))
    odd = 35
    while True:
        while prime_list[-1] < odd:   # update prime list so that it represents all primes at or below the odd number
            prime_list.append(next(prime))
        if odd != prime_list[-1]:
            if not search_primes(odd,prime_list):
                return odd
        odd += 2

if __name__=="__main__":
    from lib import timer
    print(timer.best_time(main))
