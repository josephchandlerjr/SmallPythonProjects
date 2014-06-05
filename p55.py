"""
Lychrel numbers
Problem 55

If we take 47, reverse and add, 47 + 74 = 121, which is palindromic.

Not all numbers produce palindromes so quickly. For example,

349 + 943 = 1292,
1292 + 2921 = 4213
4213 + 3124 = 7337

That is, 349 took three iterations to arrive at a palindrome.

Although no one has proved it yet, it is thought that some numbers, like 196, never produce a palindrome. A number that never forms a palindrome through the reverse and add process is called a Lychrel number. Due to the theoretical nature of these numbers, and for the purpose of this problem, we shall assume that a number is Lychrel until proven otherwise. In addition you are given that for every number below ten-thousand, it will either (i) become a palindrome in less than fifty iterations, or, (ii) no one, with all the computing power that exists, has managed so far to map it to a palindrome. In fact, 10677 is the first number to be shown to require over fifty iterations before producing a palindrome: 4668731596684224866951378664 (53 iterations, 28-digits).

Surprisingly, there are palindromic numbers that are themselves Lychrel numbers; the first example is 4994.

How many Lychrel numbers are there below ten-thousand?

NOTE: Wording was modified slightly on 24 April 2007 to emphasise the theoretical nature of Lychrel numbers.


I step through all numbers from 1 to 9999, for each checking up to 50 reverse/add calculations, if I find
one I increment a counter, at the end the number of lychrel numbers is 9999-count

"""
from lib.timer import best_time



def isPalindrome(string):
    string = str(string)
    if string == '':
        return True
    if string[0] == string[-1]:
        return isPalindrome(string[1:-1])
    else:
        return False

def reverseNumber(n):
    return int("".join(reversed(str(n))))


def main():
    count = 0
    for i in range(1,10000):
        num = i
        for _ in range(50):
            num += reverseNumber(num)
            if isPalindrome(num):
                count += 1
                break
            
    return 9999-count

print(best_time(main))
