"""
Truncatable primes
Problem 37

The number 3797 has an interesting property. Being prime itself, it is possible to continuously remove digits from left to right, and remain prime at each stage: 3797, 797, 97, and 7. Similarly we can work from right to left: 3797, 379, 37, and 3.

Find the sum of the only eleven primes that are both truncatable from left to right and right to left.

NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.
"""




def prime_generator(stop=1000000):
    primes = [None,False]+[True]*(stop-1)
    for i,prime in enumerate(primes):
        if prime:
            yield i
            primes[i+i::i] = [False]*((len(primes)-1-i)//i)

def digits_to_number(digits):
    exp = 0
    number = 0
    for d in reversed(digits):
        number += d*10**exp
        exp += 1
    return number

def number_to_digits(n):
    digits = []
    while n:
        digits.insert(0,n % 10)
        n //= 10
    return digits 

def is_truncatable(prime_number,primes):
    if prime_number < 10:
        return False
    digits = number_to_digits(prime_number)
    for d in digits[1:]:
        if d == 0 or d == 5 or d % 2 == 0:
            return False
    for i in range(1,len(digits)):
        if digits_to_number(digits[i:]) not in primes:
            return False
        if digits_to_number(digits[:i]) not in primes:
            return False
    return True


def main():     
    count = 0
    total = 0
    primes = set() 
    prime_gen = prime_generator()
    while count < 11:
        prime_number = next(prime_gen)
        primes.add(prime_number)
        if is_truncatable(prime_number,primes):
            count += 1
            total += prime_number
            #print(prime_number)
    return total

if __name__=='__main__':
    from lib.timer import best_time
    print(best_time(3,main))
