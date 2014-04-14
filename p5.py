#p5.py
#
#2520 is the smallest number that can be divided by each of the 
#numbers from 1 to 10 without any remainder.
#
#What is the smallest positive number that is evenly 
#divisible by all of the numbers from 1 to 20?


def n_gen(start=1, step=1):
    n = start 
    while True:
        yield n
        n += step

def divisible(n,numbers):
    for i in numbers:
        if n % i <> 0: 
            return False
    return True


def smallest_multiple(upper):
    """ finds smallest number that can be divided evenly into
        all integers from 1 to upper inclusive
    """
    if upper <= 1:
        return upper
    else:
        start = upper
        step = 2
        gen = n_gen(start, upper)
    numbers = range(1,20)
    for n in gen:
        if divisible(n,numbers):
            return n 

print smallest_multiple(20) 

