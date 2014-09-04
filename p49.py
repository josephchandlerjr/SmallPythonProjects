"""
Prime permutations
Problem 49

The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases by 3330, is unusual in two ways: (i) each of the three terms are prime, and, (ii) each of the 4-digit numbers are permutations of one another.

There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes, exhibiting this property, but there is one other 4-digit increasing sequence.

What 12-digit number do you form by concatenating the three terms in this sequence?

"""

def primes():
    D = {}
    q = 2
    while True:
        if q not in D:
            yield q
            D[q*q] = [q]
        else:
            for p in D[q]:
                D.setdefault(p+q,[]).append(p)
        q += 1


def find_arithmetic_sequence3(D,node=None,difference=None):
    if node == None:
        for key in D:
            res = find_arithmetic_sequence3(D,node=key,difference=None)
            if res:
                return [key]+res 
    elif difference == None:
        for key in D[node]:
            res = find_arithmetic_sequence3(D,node=key,difference=D[node][key])
            if res:
                return [key]+res
    else:
        for key in D[node]:
            if D[node][key] == difference:
                return [key]
        

def solve():
    P = {}
    results = []
    prime_numbers = primes()
    for p in prime_numbers:   #create dictionary mapping tuple(digits) to list of primes containing those digits
        if p > 1000: # only 4 digit numbers
            k = tuple(sorted(str(p)))
            P.setdefault(k,[]).append(p) 
        if p > 9999:
            break
    for key in P:
        Dist = {}  # dictionary to map v1 : {v2: v2-v1, v3: v3-v1} for all values
        for value in P[key]:
            if len(P[key]) > 3:  # must be at least 3 such primes
                Dist[value] = {}
                for value2 in P[key]:
                    if value2 > value:
                        Dist[value][value2] = value2-value
        seq = find_arithmetic_sequence3(Dist)
        if seq:
            results.append("".join(map(str,seq)))
    return results


if __name__ == '__main__':
    from lib.timer import best_time
    print(best_time(solve,_reps=2))

    
