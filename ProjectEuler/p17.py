""" Number letter counts
Problem 17

If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?

NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.

"""

def update(D, words, _range):
    for word,n in zip(words, _range):
        D[n] = word
    return D

def showD(D):
    for key in sorted(D.keys()):
        print(key,'=>',D[key]) 

def solve():
    Num2Word = {}
    from1to9 = "one two three four five six seven eight nine"
    from1to19 = "one two three four five six seven eight nine ten eleven twelve thirteen fourteen fifteen sixteen seventeen eighteen nineteen"
    from20to90by10 = "twenty thirty forty fifty sixty seventy eighty ninety"
    update(Num2Word, from1to19.split(), range(1,20))
    update(Num2Word, from20to90by10.split(), range(20,91,10))
    restrange = [n for n in range(21,100) if n%10 != 0]
    rest = [(tens + '-' + ones) for tens in from20to90by10.split() for ones in from1to9.split()]
    update(Num2Word, rest, restrange)
    from100to900by100 = [Num2Word[int(str(x)[0])]+'-hundred' for x in range(100,901,100)]
    update(Num2Word, from100to900by100, range(100, 901, 100))
    rest = [(hundreds + ' and ' + end)  for hundreds in from100to900by100 for end in [Num2Word[n] for n in range(1,100)]]
    update(Num2Word, rest, [n for n in range(101,1000) if n %100 != 0])
    Num2Word[1000] = 'one-thousand'
    strip = lambda x: [y for y in x if y not in ('-',' ')] # removes hypens
    return sum([len(strip(Num2Word[n])) for n in range(1,1001)]) 
    

if __name__ == '__main__':
    print(solve())
