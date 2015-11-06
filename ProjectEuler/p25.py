"""
1000-digit Fibonacci number
Problem 25

The Fibonacci sequence is defined by the recurrence relation:

        Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.

        Hence the first 12 terms will be:

            F1 = 1
            F2 = 1
            F3 = 2
            F4 = 3
            F5 = 5
            F6 = 8
            F7 = 13
            F8 = 21
            F9 = 34
            F10 = 55
            F11 = 89
            F12 = 144

        The 12th term, F12, is the first term to contain three digits.

        What is the first term in the Fibonacci sequence to contain 1000 digits?

"""


def fib():
    cache = {1:1,2:1}
    def memofib(n):
        try:
            return cache[n]
        except KeyError:
            res = cache[n] = fib(n-1)+fib(n-2)
            return res     
    return memofib 

fib = fib()

def solve():
    i = 12
    while True:
        if len(str(fib(i))) > 999:
            return i
        i+=1

if __name__=='__main__':
    print(solve())


