"""
Prime digit replacements
Problem 51

By replacing the 1st digit of the 2-digit number *3, it turns out that six of the nine possible values: 13, 23, 43, 53, 73, and 83, are all prime.

By replacing the 3rd and 4th digits of 56**3 with the same digit, this 5-digit number is the first example having seven primes among the ten generated numbers, yielding the family: 56003, 56113, 56333, 56443, 56663, 56773, and 56993. Consequently 56003, being the first member of this family, is the smallest prime with this property.

Find the smallest prime which, by replacing part of the number (not necessarily adjacent digits) with the same digit, is part of an eight prime value family.
"""
# will examine each prime from least to greatest until I find the smallest prime forming a set of 8 family members
# when replacing digits, only replace 0's,1's, or 2's in the number in question as if it's the lowest in set of 
# 8 members, the first replacement digits are one these three
# notes:
#
# 1. if you replace the LSD in a number with the digits 0-9 it is not possible to get a family of 8 primes as this
#
# 
# 3.if the sum of a number's digit is divisible by 3 than the number itself is divisible by 3 as well.
# let n = number, s = sum of digits of n, r = s % 3 , i = number of digits we are replacing
# when replacing one digit (d) the new remainder is going to be r + (d - d')
# upon inspections you can see that there is no way to get a family of 8 prime numbers replacing just one digit
# also if you flip i digits, the equation becoms r + i(d - d'). so i must be a muliple of 3 or again we cannot
# get enough family members. Making the brash assumption that all family members are < 10**6, we make s be 
# either 3 or 6




def primes(max=10**6):
    "prime_set(max=10**6) => set of all primes up to max inclusive"
    P = [None,False]+[True]*(max-1)
    for i in range(int(max**0.5)+1):
        if P[i]:
            P[i+i::i] = [False]*((max-i)//i)
    return [prime for prime in range(max+1) if P[prime] == True]


def digits(n):
    "returns list of digits of n as single character strings"
    n = str(n)
    return [d for d in n]


def get_indices(n):
    """
    returns all possible combinations of indices to be replaced.
    does not include index len(n)-1
    does not include a group of index unless these indices hold the
    same value
    """
    result = []
    for i in range(len(n)-1):
        for group in [x for x in result]:
            result.append(group+[i])
        result.append([i])
    return [group for group in result if len({n[g] for g in group})==1] 


def make_replacement_strings(n):
    "returns replacment strings of n"
    n = digits(n)
    indices = get_indices(n)
    result = []
    for group in indices:
        ds = n[:]
        for i in range(len(ds)):
            if i in group:
                ds[i] = '{0}'
        result.append("".join(ds))
    return result

def make_replacement_functions(n):
    result = []
    strings = make_replacement_strings(n)
    for i in range(len(strings)):
        result.append(lambda x,i=i: int(strings[i].format(x)))
    return result

def primes_by_length(max=10**6):
    """
    prime_by_length(max=10**6) 
    => two dictionaries, both map number of digits
       to corresponding primes. by_length's values are
       a list, set_by_length holds sets of these primes
    """
    by_length = {i:[] for i in range(1,7)}
    for p in primes():
        by_length[len(str(p))].append(p) 
    set_by_length = {k:set(v) for k,v in by_length.items()}
    return by_length, set_by_length 

def is_candidate(n):
    """is_candidate(integer) => True if  if 3 or 6 of the followin digits (0,1,2) else False"""
    n = str(n)
    if any(n.count(i) in (3,6) for i in ('0','1','2')):  # must have exactly 3 or 6 0's, 1's or 2's
        return True
    return False

def main():
    prime_groups, set_groups= primes_by_length()
    for g in range(1,7):
        for p in prime_groups[g]:
            if not is_candidate(p):
                continue
            functions = make_replacement_functions(p)
            for f in functions:
                count = 0 
                for i in range(10):
                    p2 = f(i)
                    if p2 in set_groups[g]:
                        count += 1
                        if count  == 8:
                            return p 


if __name__ == '__main__':
    from lib.timer import best_time 
    print(best_time(main))
