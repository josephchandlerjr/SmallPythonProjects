"""
Cubic permutations
Problem 62

The cube, 41063625 (3453), can be permuted to produce two other cubes: 56623104 (3843) and 66430125 (4053). 
In fact, 41063625 is the smallest cube which has exactly three permutations of its digits which are also cube.

Find the smallest cube for which exactly five permutations of its digits are cube.

"""
from time import time


def solve():
    n = 1
    Cubes = {}
    while True:        
        sortedCube = tuple(sorted(str(n**3)))
        try:
            if Cubes[sortedCube]['count'] == 4:
                return Cubes[sortedCube]['original']**3
            Cubes[sortedCube]['count'] += 1
        except KeyError:
            Cubes[sortedCube] = {'count': 1, 'original': n}
        n += 1

if __name__ == '__main__':
    t1 = time()
    print(solve())
    print(time() - t1)
