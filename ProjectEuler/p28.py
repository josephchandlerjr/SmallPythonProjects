
"""
Number spiral diagonals
Problem 28

Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is formed as follows:

    21 22 23 24 25
    20  7  8  9 10
    19  6  1  2 11
    18  5  4  3 12
    17 16 15 14 13

    It can be verified that the sum of the numbers on the diagonals is 101.

    What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?
"""    

# easy peasy, if we have a square grid of side-length n, the outer grid is of side lenght n+2
# just calculate the new grid side-length, add up corners and expand again until you hit 1001*1001
def solve():
    stop = 1001*1001
    current = 1
    last_length = 1
    total = 1 
    while current < stop:
        br = (current + 1) + last_length 
        side_length = last_length + 2 
        bl = br + side_length - 1
        tl = bl + side_length - 1 
        tr = tl + side_length - 1
        total += sum([br,bl,tl,tr])
        current = tr
        last_length = side_length

    return total

if __name__ == '__main__':
    print(solve())

