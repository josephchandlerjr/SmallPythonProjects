        
"""
Prime Pair Sets
Problem 60
        
        The primes 3, 7, 109, and 673, are quite remarkable. By taking any two primes and concatenating them in any order the result will always be prime. For example, taking 7 and 109, both 7109 and 1097 are prime. The sum of these four primes, 792, represents the lowest sum for a set of four primes with this property.
        
        Find the lowest sum for a set of five primes for which any two primes concatenate to produce another prime.
        reak
"""

from math import ceil, log10

def get_prime_list(stop = 10**8):
    p = [False,False]+[True]*(stop-1)
    for i in range(int(stop**0.5)+1):
        if p[i]:
            p[i+i::i] =[False]*((len(p)-1-i) // i)
    return p

def can_concat(n, m, primeSet):
    return (10**(ceil(log10(m))) * n + m) in primeSet \
           and (10**(ceil(log10(n))) * m + n) in primeSet

def get_primes():
    primeList = get_prime_list()
    primes = [i for i in range(len(primeList)) if primeList[i]]
    return primes, set(primes)

def solve():
    D = {}
    primes, primeSet = get_primes()
    primes = [p for p in primes if p < 10000]
    for i in range(len(primes)):
        D[primes[i]] = set()
        for j in range(i+1,len(primes)):
            if can_concat(primes[i], primes[j], primeSet):
                D[primes[i]].add(primes[j])
    min, min_set = 10**10, None
    for a in primes:
        if a > min:
            break
        for b in D[a]:
            if a+b > min:
                continue
            workingB = D[a] & D[b]
            for c in workingB:
                if a+b+c > min:
                    continue
                workingC = workingB & D[c]
                for d in workingC:
                    if a+b+c+d > min:
                        continue
                    workingD = workingC & D[d]
                    for e in workingD:
                        if a+b+c+d+e > min:
                            continue
                        min, min_set = a+b+c+d+e, (a,b,c,d,e) 
    return min, min_set



if __name__ == '__main__':
    from time import time
    t1=time()
    print(solve())
    print(time()-t1)
