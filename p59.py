from urllib.request import urlopen
from itertools import permutations



# make set out of common words in lib for easy searching
common_words = set(open('./lib/commonWords', 'r').read())


def generate(p):
    'a generator cycling through iterable P yielding its items'
    while True:
        for item in p:
            yield item



# download cypher from project euler
cipher = list(map(lambda x: int(x),urlopen('http://projecteuler.net/project/resources/p059_cipher.txt').readline().decode().rstrip().split(',')))
# get all possible 3 digit keys consisting on lowercase letters a-z (97-122)
possible_keys = permutations(range(97,123), 3)

possible_answers = []

def decipher():

    for key in possible_keys:
        sum = 0
        result = ''
        k = generate(key)
        for code in cipher:
            new_ord = code ^ next(k)
            if new_ord > 126:
                continue                   # assume ascii encoding 
            sum += new_ord
            result += chr(new_ord)
        if 'Word' in result:
            return sum
            return

solve = decipher

if __name__=='__main__':
    print(solve())
