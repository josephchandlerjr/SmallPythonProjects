"""
Lattice paths
Problem 15

Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom 
right corner.
How many such routes are there through a 20×20 grid?
"""

def solve():
    D = {}
    for row in range(21):
        D[(row, 20)] = 1
    for col in range(21):
        D[(20, col)] = 1
    for row in range(19, -1, -1):
        for col in range(19, -1, -1):
            D[(row, col)] = D[(row+1, col)] + D[(row, col+1)]
    return D[(0,0)]

if __name__ == '__main__':
    print(solve())
