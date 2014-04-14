#!/usr/bin/env python
#if the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
#
#If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?
#
#NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) 
#contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. 
#The use of "and" when writing out numbers is in compliance with British usage.


from1to19 = "one two three four five six seven eight nine ten eleven twelve thirteen fourteen fifteen sixteen seventeen eighteen nineteen"
from1to19 = zip(range(1,20),from1to19.split()) 
num2word = dict((n,w) for n,w in from1to19)
from20to90by10 = "twenty thirty forty fifty sixty seventy eighty ninety"
from20to90by10 = zip(range(20,91,10),from20to90by10.split())
num2word.update(dict((n,w) for n,w in from20to90by10))
from21to99 = [(n,w) for n,w in zip([n for n in range(21,100) if n%10!=0],[(pre+'-'+num2word[ones_place]) \
                for pre in [x[1] for x in from20to90by10] for ones_place in range(1,10)])]
num2word.update(dict((n,w) for n,w in from21to99))
from100to900by100 = zip(range(100,901,100),[num2word[int(str(x)[0])]+'-hundred' for x in range(100,901,100)])
num2word.update(dict((n,w) for n,w in from100to900by100))
num2word.update(dict((n,w) for n,w in zip([n for n in range(101,1000) if n%100!=0], [(hundred +' and '+ rest) for hundred in \
        [n[1] for n in from100to900by100] for rest in [num2word[x] for x in range(1,100)]])))
num2word[1000] = 'one-thousand'
strip = lambda x: [y for y in x if y not in ('-',' ')]
print sum([len(strip(num2word[n])) for n in range(1,1001)]) 
