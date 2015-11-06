"""
Coded triangle numbers
Problem 42

The nth term of the sequence of triangle numbers is given by, tn = ½n(n+1); so the first ten triangle numbers are:

    1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

By converting each letter in a word to a number corresponding to its alphabetical position and adding these values we form a word value. For example, the word value for SKY is 19 + 11 + 25 = 55 = t10. If the word value is a triangle number then we shall call the word a triangle word.

Using words.txt (right click and 'Save Link/Target As...'), a 16K text file containing nearly two-thousand common English words, how many are triangle words?

"""
from string import ascii_uppercase

L = dict(zip(ascii_uppercase,range(1,len(ascii_uppercase)+1))) # maps letter to its value

V = {}  # maps a value to a set of words

def word_value(word):
    return sum([L[letter] for letter in word if letter != '"'])

def triangle_number(n):
    return (n*(n+1))//2

def solve():
    max_value = 0
    for line in open('./lib/words.txt'):
        line = line.rstrip()
        for word in line.split(','):
            value = word_value(word)
            if value > max_value: max_value = value 
            try:
                V[value].add(word)
            except KeyError:
                V[value] = {word}

    return sum(len(V[value]) for value in V.keys() if value in [triangle_number(n) for n in range(1,max_value)])


if __name__=='__main__':
    from lib.timer import best_time
    print(best_time(solve))
