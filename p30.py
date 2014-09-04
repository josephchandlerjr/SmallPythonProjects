"""
Digit fifth powers
Problem 30

Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:

1634 = 1^4 + 6^4 + 3^4 + 4^4
8208 = 8^4 + 2^4 + 0^4 + 8^4
9474 = 9^4 + 4^4 + 7^4 + 4^4

As 1 = 14 is not a sum it is not included.

The sum of these numbers is 1634 + 8208 + 9474 = 19316.

Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.

"""

# max value for any base 10 number is 10**n - 1 where n = # of digits in the number
# max value for the sum of the fifth powers of a numbers digis is n*9**5
# the inequality defining upper bound is 10**n - 1 > n*9**5. 
# the left side grows exponentially while the right side grows linearly


from itertools import combinations_with_replacement as c

test = lambda n: (10**n - 1)/9**5 

def find_upper_bound(power):
    n = 1
    while test(n) < n:
        n+=1
    return n

upper_bound = find_upper_bound(5)

def find_upper_bound2(power):
    n = 1
    while test(n) < n:
        n+=1
    return n*9**5


upper2 = find_upper_bound2(5)



# check all combinations of 7 digit numbers

def solve():
    res = -1 
    for num_length in range(1,upper_bound+1):    
        combos = c(range(10),num_length)
        for combo in combos:
            total = sum([x**5 for x in combo])
            if sorted([x for x in str(total)]) == sorted(map(str,combo)):
                res+=total
    return res



if __name__ == '__main__':
    print(solve())




