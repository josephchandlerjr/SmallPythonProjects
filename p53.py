"""
Combinatoric selections
Problem 53

There are exactly ten ways of selecting three from five, 12345:

    123, 124, 125, 134, 135, 145, 234, 235, 245, and 345

    In combinatorics, we use the notation, 5C3 = 10.

    In general,
    nCr =   
    n!/
    r!(n−r)!
        ,where r ≤ n, n! = n×(n−1)×...×3×2×1, and 0! = 1.

        It is not until n = 23, that a value exceeds one-million: 23C10 = 1144066.

        How many, not necessarily distinct, values of  nCr, for 1 ≤ n ≤ 100, are greater than one-million?

"""
#    1
#   1 1
#  1 2 1
# 1 3 3 1
#1 4 6 4 1 
#

def main():
    row = [] 
    count = 0
    for n in range(1,101):
        new_row = [1]
        prev = 1
        for k in row[1:]:
            value = prev+k
            if value > 1000000:
                count += 1
            new_row.append(value)
            prev = k
        new_row.append(1)
        row = new_row

    return count

if __name__ == '__main__':
    from lib.timer import best_time
    print(best_time(main))
