#utils3.py


def decrement_pandigital(n):
    """
    decrement_pandigital(n) => n-1 as a string
    n is a known pandigital number(string or int)
    will break if decrement below its lowest permutation
    """
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

    

