"""
Pandigital multiples
Problem 38

Take the number 192 and multiply it by each of 1, 2, and 3:

        192 × 1 = 192
        192 × 2 = 384
        192 × 3 = 576

By concatenating each product we get the 1 to 9 pandigital, 192384576. We will call 192384576 the concatenated product of 192 and (1,2,3)

The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, and 5, giving the pandigital, 918273645, which is the concatenated product of 9 and (1,2,3,4,5).

What is the largest 1 to 9 pandigital 9-digit number that can be formed as the concatenated product of an integer with (1,2, ... , n) where n > 1?

"""

# largest pandigital number is 987654321
# we know our lower bound is 918273645 referenced in the problems description
# we can work backwards and see if a pandigital number can be divided evenly into a sequence of integers (1,2,  ... , n)
#1234 1243 1

class PandigitalNumber:
    """
    Internally, attributes are stored as strings but increment and decrement
    methods return integer
    """
    def __init__(self,number=123456789):
        self.number = str(number)
        self.min = "".join(sorted(self.number))
        self.max = "".join(reversed(sorted(self.number)))

    def is_max(self):
        return self.number == self.max

    def is_min(self):
        return self.number == self.min
    
    def decrement(self):
        """
        Decrements self.number to the next lowest pandigital number.
        Raises AttributeError if if is already lowest positive pandigital of this size 
        """
        if self.is_min():
            raise AttributeError('{} the is least pandigital number in sequence'.format(self.number))
        string = self.number 
        to_swap = 0
        # searching from right to left, find first digit that is larger than
        # digit immediately to the right of it and is not a '1'
        # this is the digit we need to decrement
        for i in range(len(string)-1,0,-1):
            if string[i-1] > string[i]  and string[i-1] != '1':
                to_swap = i-1
                break
        msd = string[:to_swap]
        lsd = "".join(reversed(sorted(string[to_swap+1:])))
        digit = string[to_swap]
        for other_digit in lsd:
            if digit > other_digit:
                digit,lsd = other_digit, lsd.replace(other_digit,digit)
                break                
        self.number = msd+digit+lsd
        return int(self.number) 

    def increment(self):
        """
        Increments self.number to the next highest pandigital number.
        Raises AttributeError if if is already highest pandigital of this size 
        """

        if self.is_max():
            raise AttributeError('{} is the greatest pandigital number in sequence'.format(self.number))
        string = self.number
        to_swap = 0
        for i in range(len(string)-1,0,-1):
            if string[i] > string[i-1]:
                to_swap = i-1
                break
        msd = string[:to_swap]
        lsd = "".join(sorted(string[to_swap+1:]))
        digit = string[to_swap]
        for other_digit in lsd:
            if digit < other_digit:
                digit,lsd = other_digit, lsd.replace(other_digit,digit)
                break                
        self.number = msd+digit+lsd
        return int(self.number) 

def decrement_pandigital(n):
    string = str(n)  
    to_swap = 0
    for i in range(len(string)-1,0,-1):
        if string[i-1] > string[i] and string[i-1] != '1':
            to_swap = i-1
            break
    msd = string[:to_swap]
    lsd = "".join(reversed(sorted(string[to_swap+1:])))
    digit = string[to_swap]
    for other_digit in lsd:
        if digit > other_digit:
            digit,lsd = other_digit, lsd.replace(other_digit,digit)
            break                
    return  msd+digit+lsd

def is_pan_multiple(n):
    # find if ther are two leading,subsequent substrings that where substringA * 2 = substring B
    # if not return False
    n = str(n)
    multiplicand = None
    for i in range(1,len(n)):
        mult, rest = n[0:i], n[i:] 
        product = int(mult) * 2
        if rest.startswith(str(product)):
            multiplicand = int(mult)
            break
    if not multiplicand:
        return False
    n = n[i+len(str(product)):]
    multiplier = 3
    #now eliminated substrings that are muliples of multiplicand
    while n: 
        product = multiplicand * multiplier
        if n.startswith(str(product)):
            n = n[len(str(product)):]
            multiplier += 1
        else:
            return False
    return True

def main2():
    """
    uses PandigitalNumber class
    """
    PN = PandigitalNumber(987654321)
    while True:
        if is_pan_multiple(PN.number):
            return PN.number
        else:
            PN.decrement()

def main():
    PN = '987654321'
    while True:
        if is_pan_multiple(PN):
            return PN
        else:
            PN = decrement_pandigital(PN)

def count_up(pn,reps=10):
    for _ in range(reps):
        print(pn.number)
        pn.increment() 

def count_down(pn,reps=10):
    for _ in range(reps):
        print(pn.number)
        pn.decrement() 
   
def test_increment():
    pn = PandigitalNumber()
    count_up(pn)

def test_decrement():
    pn = PandigitalNumber(987654321)
    count_down(pn) 

solve = main
if __name__=='__main__':
    from lib.timer import best_time
    print(best_time(main))
    print(best_time(main2))

