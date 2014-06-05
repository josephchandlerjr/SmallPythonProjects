"""
Powerful digit sum
Problem 56

A googol (10100) is a massive number: one followed by one-hundred zeros; 100100 is almost unimaginably large: one followed by two-hundred zeros. Despite their size, the sum of the digits in each number is only 1.

Considering natural numbers of the form, ab, where a, b < 100, what is the maximum digital sum?


"""

def digit_sum(n):
    sum = 0
    while n:
        sum += n % 10
        n //= 10
    return sum

max = 0
for a in range(1,100):
    for b in range(1,100):
         sum = digit_sum(a**b)
         if max < sum: max = sum

print(max)
