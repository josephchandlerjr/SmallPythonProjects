"""
Quadratic primes
Problem 27

Euler discovered the remarkable quadratic formula:

    n² + n + 41

    It turns out that the formula will produce 40 primes for the consecutive
    values n = 0 to 39. However, when n = 40, 402 + 40 + 41 = 40(40 + 1) + 41 
    is divisible by 41, and certainly when n = 41, 41² + 41 + 41 is 
    clearly divisible by 41.

    The incredible formula  n² − 79n + 1601 was discovered, 
    which produces 80 primes for the consecutive values n = 0 to 79. 
    The product of the coefficients, −79 and 1601, is −126479.

    Considering quadratics of the form:

            n² + an + b, where |a| < 1000 and |b| < 1000

                where |n| is the modulus/absolute value of n
                    e.g. |11| = 11 and |−4| = 4

                    
                    
    Find the product of the coefficients, a and b, for the quadratic 
    expression that produces the maximum number of primes for 
    consecutive values of n, starting with n = 0.
    """

def formula(a,b):
    'returns function f(n) which returns n² + an + b'
    return lambda n: n**2 + a*n + b

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
                numbers[i*2::i] = [False] * ((stop-1)//i - 1) 
            else:
                return numbers

primes = prime_generator(1000)
def is_prime(n):
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

# b must be prime so that n=0 works
# when n = 1, n**2 + an + b == 1 + n + b so this also must be prime
# in order for the coefficient on n**2 to be 1 the form must be (n+x)(n+y) so in
# n**2 + an + b , a = x+y  and b = xy

def solve():
    longest = (0,0,0)
    for a in range(-1000,1001):
        for b in range(-1000,1001):
            if is_prime(b) and is_prime(1 + a + b):
                f = formula(a,b)
                n = 0
                while is_prime(f(n)):
                    n +=1
                longest = n > longest[0] and (n, a, b) or longest
    max_num_primes, a, b = longest
    product = a * b
    return 'The maximum number of primes produced is {0}\n(a,b) = ({1},{2})\n a * b = {3}'.format(max_num_primes, a, b, product)



if __name__ == '__main__':
    print(solve())
