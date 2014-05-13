"""
p1.py
If we list all the natural numbers below 10 that are multiples of 
3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.

"""
def sum_of_multiples(m,n):
    """
    sum_of_multiples(m,n) => sum(multiples of m <= n)
    """
    number_of_multiples = (n-1)//m
    return sum(m*i for i in range(1,number_of_multiples+1))

def brute():
    return sum([n for n in range(1000) if n%3 == 0 or n%5 == 0])

def eloquent(n=1000):
    sum3,sum5,sum15 = map(sum_of_multiples,(3,5,15),(n,)*3)
    return sum3+sum5-sum15

if __name__=='__main__':
    from lib.timer import best_time
    b,e = map(best_time,(brute,eloquent))
    print(b,'\n',e)
