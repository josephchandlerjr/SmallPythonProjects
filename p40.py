"""
Champernowne's constant
Problem 40

An irrational decimal fraction is created by concatenating the positive integers:

    0.12345678910'1'112131415161718192021...

    It can be seen that the 12th digit of the fractional part is 1.

    If dn represents the nth digit of the fractional part, find the value of the following expression.

    d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000

"""

def integers():
    i = 1
    while True:
        digits = []
        j = i
        while j:
            digits.append(j % 10)
            j //= 10
        yield i
        i +=1

def brute():
    L= ['.']
    ints = integers()
    while len(L) < 1000001:
        integer = next(ints)
        digits = []
        while integer:
            digits.insert(0,integer % 10)
            integer //= 10
        for d in digits:
            L.append(d)

    ns = (L[1],  L[10] , L[100] , L[1000] , L[10000] , L[100000] , L[1000000])
    total = 1
    for n in ns:
        total *= n
    return total

def eloquent():
    # find some indexes we know 
    # end at last n-digit number so say 
    I = {1:1,9:9}
    last_known_index= 9
    last_known_value = 9
    n = 2
    while 10**n < 1000000:
        value = 10**n -1
        offset = value - last_known_value
        index = last_known_index + offset * n  
        I[index] = value
        last_known_index,last_known_value = index,value
        n += 1
    total = 1
    known_indices = list(reversed(sorted(I.keys())))
    for index in (1,10,100,1000,10000,100000,1000000):
        if index < 10:
            total *= index 
        else:
            # get appropriate known index
            # offset = (index_in_question - known_index)//number of digits  
            # offset + prev value + 1
            for known in known_indices:
                if index >= known:
                    known_value,known_index = I[known],known
                    offset = index-known_index
                    digits = len(str(known_value))+1
                    number = (offset//digits) + known_value+1
                    remainder = offset % digits
                    total *= int(str(number)[remainder-1])
                    break
    return total           

                    

if __name__=='__main__':
    from lib.timer import best_time
    print(best_time(eloquent))


    print(best_time(brute))
