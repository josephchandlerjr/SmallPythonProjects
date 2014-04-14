#p11.py
# _*_ coding: UTF-8 _*_ 
#In the 20×20 grid below 
#
#What is the greatest product of four adjacent numbers in the same direction (up, down, left, right, or diagonally) in the 20×20 grid?
import sys

class Point(object):
    def __init__(self,index,value,neighbors):
        self.index = index
        self.value = value
        self.neighbors = neighbors
        
class Grid(list):
    """
    a square grid
    
    """

    directions = ('left', 'right', 'up', 'down', 'lower_left', 'lower_right', 'upper_left', 'upper_right')

    def __init__(self,grid):
        super(Grid,self).__init__()
        grid = map( int,grid.strip().split() )
        self.rows = int(len(grid)**0.5)
        self.columns = self.rows
        for i,val in enumerate(grid):
            self.append(Point(i,val,{}))
        for point in self:
            neighbors = map(lambda i: None if i == None else self[i], self.neighbors(point.index))
            point.neighbors= dict( zip(self.directions,neighbors) )

    def is_first_column(self, i):
        return i % self.columns == 0
    
    def is_last_column(self, i): 
        return i % self.columns == self.columns-1 
    
    def is_first_row(self, i):
        return i < self.columns
    
    def is_last_row(self, i): 
        return i >= (self.columns * (self.rows-1) )

    def upper_right(self, i):
        """finds index up and to the right of index i
           if no such index exists return None"""
        if self.is_first_row(i) or self.is_last_column(i):
            return None
        else:
            return i-self.columns-1

    def upper_left(self, i):
        if self.is_first_row(i) or self.is_first_column(i):
            return None
        else:
            return i-self.columns+1

    def lower_right(self, i):
        if self.is_last_row(i) or self.is_last_column(i):
            return None
        else:
            return i+self.columns+1

    def lower_left(self, i):
        if self.is_last_row(i) or self.is_first_column(i):
            return None
        else:
            return i+self.columns-1

    def up(self, i):
        if self.is_first_row(i):
            return None
        else:
            return i-self.columns
        
    def down(self, i):
        if self.is_last_row(i):
            return None
        else:
            return i+self.columns

    def up(self, i):
        if self.is_first_row(i):
            return None
        else:
            return i-self.columns

    def left(self, i):
        if self.is_first_column(i):
            return None
        else:
            return i-1

    def right(self, i): 
        if self.is_last_column(i):
            return None
        else:
            return i+1

    def neighbors(self,i): 
        return (self.left(i), self.right(i), self.up(i), self.down(i), self.lower_left(i), 
                self.lower_right(i), self.upper_left(i), self.upper_right(i) )

    def get_row(self,point,direction,size=4):
        row = [point] 
        move = getattr(self,direction)
        for _ in range(size-1):
            current_point = row[-1]
            neighbor = move(current_point.index)
            if neighbor == None:
                return row
            row.append(self[neighbor])
        return row

if __name__ == '__main__':
    from operator import mul

    grid = """
    08 02 22 97 38 15 00 40 00 75 04 05 07 78 52 12 50 77 91 08
    49 49 99 40 17 81 18 57 60 87 17 40 98 43 69 48 04 56 62 00
    81 49 31 73 55 79 14 29 93 71 40 67 53 88 30 03 49 13 36 65
    52 70 95 23 04 60 11 42 69 24 68 56 01 32 56 71 37 02 36 91
    22 31 16 71 51 67 63 89 41 92 36 54 22 40 40 28 66 33 13 80
    24 47 32 60 99 03 45 02 44 75 33 53 78 36 84 20 35 17 12 50
    32 98 81 28 64 23 67 10 26 38 40 67 59 54 70 66 18 38 64 70
    67 26 20 68 02 62 12 20 95 63 94 39 63 08 40 91 66 49 94 21
    24 55 58 05 66 73 99 26 97 17 78 78 96 83 14 88 34 89 63 72
    21 36 23 09 75 00 76 44 20 45 35 14 00 61 33 97 34 31 33 95
    78 17 53 28 22 75 31 67 15 94 03 80 04 62 16 14 09 53 56 92
    16 39 05 42 96 35 31 47 55 58 88 24 00 17 54 24 36 29 85 57
    86 56 00 48 35 71 89 07 05 44 44 37 44 60 21 58 51 54 17 58
    19 80 81 68 05 94 47 69 28 73 92 13 86 52 17 77 04 89 55 40
    04 52 08 83 97 35 99 16 07 97 57 32 16 26 26 79 33 27 98 66
    88 36 68 87 57 62 20 72 03 46 33 67 46 55 12 32 63 93 53 69
    04 42 16 73 38 25 39 11 24 94 72 18 08 46 29 32 40 62 76 36
    20 69 36 41 72 30 23 88 34 62 99 69 82 67 59 85 74 04 36 16
    20 73 35 29 78 31 90 01 74 31 49 71 48 86 81 16 23 57 05 54
    01 70 54 71 83 51 54 69 16 92 33 48 61 43 52 01 89 19 67 48
    """

    grid = Grid(grid)
    greatest_product = 0
    best_row = []
    for point in grid:
        candidates = [r for r in [grid.get_row(point,d) for d in grid.directions] if len(r) == 4]
        for row in candidates:
            value = reduce(mul,[p.value for p in row])
            if value > greatest_product:
                greatest_product, best_row = value, row

    print greatest_product
    print best_row
