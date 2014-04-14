# let r = number of rows
# let c = number of columns
# let n(i) = number of paths down from row i
# c+1             )   if i == 0 
# n(i-1)           >   if i == r
# 2*n(i-1) -1     )   else     
#

from p11v3 import *
from math import factorial
from time import time

def lattice_paths(grid):
    frontier = [grid[0]]
    count = 0

    while frontier:
        p = frontier.pop(0)
        
        right = p.neighbors['right']
        if grid.is_last_column(right.index):
            count +=1
        else:
            frontier.append(right)

        down = p.neighbors['down']
        if grid.is_last_row(down.index):
            count +=1
        else:
            frontier.append(down)

    return count

for x in range(3,11):
    grid = make_grid(x,x)
    print x, '   ', lattice_paths(grid)

print """
The above loops shows the central binomial coefficient sequence 
which makes sense.
For an NxN grid, all paths will have size 2N. 
N 'downs' and R 'rights'.
If you remove all 'downs' from the sequence, we know the sequence of 'rights'.
Therefore, the question is, if you have 2N items, 
how many ways can you choose N of
them. And that of course is (2n)!/( (n!)**2)
"""

print 'In a 20 x 20 grid there are %d possible paths.' %(factorial(40)/( factorial(20)**2))

print """
 using dynamic programming
 in a 20 x 20 graph there are 21*21 nodes
 starting from the finishing node in the lower right corner
 we can work backwards to find the total number of paths.
"""

def label_nodes(grid):
    frontier = [grid[-1]]
    #first label all bottom and right side nodes
    bottom_left = grid.columns * (grid.rows-1)
    bottom_right = grid[-1].index
    for i in range(bottom_left,bottom_right+1):
        grid.update(grid[i],1)
    top_right = grid.columns-1
    for i in range(top_right,bottom_right+1,grid.columns):
        grid.update(grid[i],1)
    start = bottom_right-grid.columns-1
    for i in range(start,-1,-1):
        if not grid.is_last_column(i):
            right = grid[i].neighbors['right'].value
            down = grid[i].neighbors['down'].value
            grid.update(grid[i], right + down )
    return grid    

grid = make_grid(21,21)
t1 = time()
grid = label_nodes(grid)
print 'Dynamic programming yields %s in %f seconds' %(grid[0].value, time()-t1)




