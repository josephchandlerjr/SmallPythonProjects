"""
Permuted multiples
Problem 52

It can be seen that the number, 125874, and its double, 251748, contain exactly the same digits, but in a different order.

Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain the same digits.


"""
# note the diffence between two permutation in base 10 is always a multiple
# of 9. Example:  xyz - zxy = 100x + 10y + 1z - 100z + 10x + 1y
#                           = (100x - 10x) + (10y - y) + (z-100z)
#                           = 90x + 9y - 99z
#                           = 9(10x + y - 11z)
# or simple see that if digit = d*10^i and is changed to d*10^j , you
# can ignot the 'd' an simple calculat 10^j - 10^i which is always a multiple of 9


from time import time

def _sorted(n):
    return sorted(str(n))

def check(n,base):
    for m in range(3,7):
        if not _sorted(m*n) == base: 
            return False
    return True

def main():
    n = 9 
    while True:
        base = _sorted(n)
        if base == _sorted(n+n):
            if check(n,base):
                return n
        n+=9
t = time()
print(main())
print(time()-t)
