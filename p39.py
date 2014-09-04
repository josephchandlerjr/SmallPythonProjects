"""
Integer right triangles
Problem 39

If p is the perimeter of a right angle triangle with integral length sides, {a,b,c}, there are exactly three solutions for p = 120.

{20,48,52}, {24,45,51}, {30,40,50}

For which value of p ≤ 1000, is the number of solutions maximised?

"""
from collections import defaultdict
from time import sleep 

P = defaultdict(int)

for a in range(1,1000):
    for b in range(1,1000):
        if a >= b and (a+b<1000):
            c = (a**2+b**2)**0.5
            if a+b+c <= 1000:
                if int(c) == c:
                    P[a+b+c]+=1

def solve():
    return max(P.keys(),key=lambda x: P[x])

if __name__ == '__main__':
    print(solve())


