"""
Consecutive prime sum
Problem 50

The prime 41, can be written as the sum of six consecutive primes:
    41 = 2 + 3 + 5 + 7 + 11 + 13

    This is the longest sum of consecutive primes that adds to a prime below one-hundred.

    The longest sum of consecutive primes below one-thousand that adds to a prime, contains 21 terms, and is equal to 953.

    Which prime, below one-million, can be written as the sum of the most consecutive primes?

"""



def prime_gen(stop=10**6):
    P = [None,None]+[True]*(stop-1)
    for i in range(len(P)):
        if P[i]:
            yield i
            if i < int(stop**0.5+1):
                P[i+i::i] = [False]*((stop-i)//i)


def main():
    # create list of sums where prime_sum[i] = sum from first prime up to prime number i
    # example prime_sum[2] = 2 prime_sum[3] = 5 prime_sum[5] = 10 ...
    prime_sum =  [0]
    primes = []
    total = 0
    for p in prime_gen():
        total += p
        prime_sum.append(total)
        primes.append(p)

    prime_set = set(primes)  # for searching
    # now sum from i to j is prime_sum[j] - prime_sum[i]  
    best_length = 0
    for i in range(len(primes)):
        for j in range(i+best_length,len(primes)):
            sum = prime_sum[j] - prime_sum[i]
            if sum > 1000000:
                break
            if j-i > best_length and sum in prime_set:
                best_length, best_sum = j-i, sum

    return best_sum


if __name__=='__main__':
    from lib.timer import best_time
    print(best_time(main,_reps=3))
