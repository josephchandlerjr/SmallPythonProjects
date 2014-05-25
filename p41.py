"""
Pandigital prime
Problem 41

We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital and is also prime.

What is the largest n-digit pandigital prime that exists?

"""

# not number is divisible by 3 if the sum of its digits is divisible by 3
# all pandigital number except those of length 4 or 7 are divisible by 3

def is_pandigital(n):
    string = str(n)
    return sorted(string) == is_pandigital.match[len(string)] 
     
is_pandigital.match = {4: sorted('1234'), 7: sorted('1234567')}
    
def prime_list(stop):
    p = [False,False]+[True]*(stop-1)
    for i in range(int(stop**0.5)+1):
        if p[i]:
            p[i+i::i] =[False]*((len(p)-1-i) // i)
    return p

def main():
    primes = prime_list(stop=7654321)
    start_stop_step = ( (7654321,1234568,-1),(4321,1235,-1) )
    for start,stop,step in start_stop_step:
        for i in range(start,stop,step):
            if primes[i] and is_pandigital(i):
                return i
    return None 

if __name__=='__main__':
    from lib.timer import best_time
    print(best_time(main))
    
