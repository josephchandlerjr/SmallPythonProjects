"""
Self powers
Problem 48

The series, 1^1 + 2^2 + 3^3 + ... + 10^10 = 10405071317.

Find the last ten digits of the series, 11 + 22 + 33 + ... + 10001000.

"""

def just10mult(n,m):
    """ 
    multiplies n*m until 10 LSD are known, returns those digits
    """
    total = 0
    cycles = 10
    for c in range(cycles):
        if n:
            multiplier = (n%10)*10**c 
            total += multiplier * m
            n //= 10
    return total


#a = 12345678999776
#b = 123456789987654
#print(str(a*b)[-10:] == str(just10mult(a,b))[-10:])



def solve():
    total = 0
    mod = 10**10
    for n in range(1,1001):
        total += n**n
    return str(total)[-10:]




if __name__ == '__main__':
    from lib.timer import best_time
    print(best_time(solve,_reps=2))
