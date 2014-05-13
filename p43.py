"""
Sub-string divisibility
Problem 43

The number, 1406357289, is a 0 to 9 pandigital number because it is made up of each of the digits 0 to 9 in some order, but it also has a rather interesting sub-string divisibility property.

Let d1 be the 1st digit, d2 be the 2nd digit, and so on. In this way, we note the following:

d2d3d4=406 is divisible by 2
d3d4d5=063 is divisible by 3
d4d5d6=635 is divisible by 5
d5d6d7=357 is divisible by 7
d6d7d8=572 is divisible by 11
d7d8d9=728 is divisible by 13
d8d9d10=289 is divisible by 17

Find the sum of all 0 to 9 pandigital numbers with this property.


"""


pandigits = {x for x in range(10)}

def is_pandigital(n,length=10,pansdigits=pandigits,truncate=True):
    """
    is_pandigital(n,length=10,pansdigits=pandigits,truncate=True)
    => n if n pandigital 0 .. length-1 else False
    """
    n = str(n)
    if sorted(n) == list(map(str,range(length))):
        return int(n)
    return False

def main():
    candidates = [str(i) for i in range(123,988) if i % 17 == 0 if len(set(str(i))) == len(str(i)) ]# start with all multiples of 17 

    for mult in (13,11,7,5,3,2): # each multiple 
        new_candidates = []
        for candidate in candidates:
            digits = [x for x in candidate] # list of str(digit) for each digit in candidate
            for i in range(10):   
                i = str(i)
                if i not in digits: # if i is in in digits, this wouldnt be pandigital
                    new_number = int(i+digits[0]+digits[1])
                    if new_number % mult == 0:
                        new_candidates.append(i+candidate) 

        candidates = new_candidates

    total = 0
    for candidate in candidates:
        for n in range(1,10):
            n = str(n)
            if n not in candidate:
                total += int(n+candidate)
    return total
        

if __name__=='__main__':
    from lib.timer import best_time
    print(best_time(main))
