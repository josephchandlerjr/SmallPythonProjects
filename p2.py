#p2.py
#Each new term in the Fibonacci sequence is generated 
#by adding the previous two terms. By starting with 1 and 2, 
#the first 10 terms will be:

#    1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

#   By considering the terms in the Fibonacci sequence 
#whose values do not exceed four million, find the sum 
#of the even-valued terms.


limit = 4 * 10**6

def fib_gen():
    last = 1
    yield last
    current = 2
    yield current
    while True:
        current,last = current+last, current
        yield current

fibs = fib_gen()

s = 0
for n in fibs:
    if n <= limit:
        if n%2 == 0:
            s+= n
    else:
        print s
        break





