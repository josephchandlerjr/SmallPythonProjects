"""
Names scores
Problem 22
Published on Friday, 19th July 2002, 06:00 pm; Solved by 68973

Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names, begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, multiply this value by its alphabetical position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would obtain a score of 938 × 53 = 49714.

What is the total of all the name scores in the file?

"""

from string import ascii_lowercase as lowercase


def solve():
    global lowercase
    f = open('./lib/names.txt', 'r')
    names = f.read().split(',')
    f.close()
    names.sort()
    lowercase = 'X'+lowercase
    def name_value(name):
        result = 0
        name = name.lower().strip()
        for char in name:
            if char != '"':
                result += lowercase.index(char) 
        return result

    return sum(name_value(name)*(i+1) for i,name in enumerate(names))

if __name__ == '__main__':
    print(solve())
    
