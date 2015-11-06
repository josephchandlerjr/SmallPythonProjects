def prime_gen(stop=10**6):
    P = [None,None]+[True]*(stop-1)
    for i in range(len(P)):
        if P[i]:
            yield i
            if i < int(stop**0.5+1):
                P[i+i::i] = [False]*((stop-i)//i)

primes= list(prime_gen())
prime_set=set(primes)

def is_prime(n):
    return n in prime_set

prime_sum = [0]

sum = 0
count = 0
while (sum < 10**6):
    sum+=primes[count]
    prime_sum.append(sum)
    count+=1

terms = 1
for i in range(count):
    for j in range(i+terms, count):
        n = prime_sum[j] - prime_sum[i]
        if (j-i>terms and is_prime(n)):
            (terms,max_prime) = (j-i,n)  # keeps expanding 'terms'

print("Answer to Problem 50 = ",max_prime," with ",terms," terms\n")

