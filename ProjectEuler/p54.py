"""
Poker hands
Problem 54

In the card game poker, a hand consists of five cards and are ranked, from lowest to highest, in the following way:

High Card: Highest value card.
One Pair: Two cards of the same value.
Two Pairs: Two different pairs.
Three of a Kind: Three cards of the same value.
Straight: All cards are consecutive values.
Flush: All cards of the same suit.
Full House: Three of a kind and a pair.
Four of a Kind: Four cards of the same value.
Straight Flush: All cards are consecutive values of same suit.
Royal Flush: Ten, Jack, Queen, King, Ace, in same suit.

                                            The cards are valued in the order:
                                            2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, King, Ace.

 If two players have the same ranked hands then the rank made up of the highest value wins; for example, a pair of eights beats a pair of fives (see example 1 below). But if two ranks tie, for example, both players have a pair of queens, then highest cards in each hand are compared (see example 4 below); if the highest cards tie then the next highest cards are compared, and so on.
The file, poker.txt, contains one-thousand random hands dealt to two players. Each line of the file contains ten cards (separated by a single space): the first five are Player 1's cards and the last five are Player 2's cards. You can assume that all hands are valid (no invalid characters or repeated cards), each player's hand is in no specific order, and in each hand there is a clear winner.  How many hands does Player 1 win?  
"""

from itertools import combinations


# just for kicks let's use OOP 


class Hand:
    """
    class Hand:  object representation of a poker hand
    initialized with a list of strings representing 5 cards as 
    card/suit separated by spaces like so 3D 6D 7H QD QS
    suits are S,H,D, or C
    cards are 23456789TJQKA
    
    possible categories and their score are :
    SCORE     HAND            DESCRIPTION
    0       High Card         Highest value card.
    1       One Pair          Two cards of the same value.
    2       Two Pairs         Two different pairs.
    3       Three of a Kind   Three cards of the same value.
    4       Straight          All cards are consecutive values.
    5       Flush             All cards of the same suit.
    6       Full House        Three of a kind and a pair.
    7       Four of a Kind    Four cards of the same value.
    8       Straight Flush    All cards are consecutive values of same suit.
    9       Royal Flush       Ten, Jack, Queen, King, Ace, in same suit.
   
    """
    tests = ('isRoyalFlush','isStraightFlush','isFourOfAKind',
             'isFullHouse','isFlush','isStraight','isThreeOfAKind',
             'isTwoPair','isPair'
            )

    def __init__(self,cards):
        self.cards = cards
        self.ranks = list(reversed(sorted(self.getHandValues(cards))))   # greatest --> smallest
        self.suits = [card[1] for card in cards]
        self.value = (0,self.ranks)  # initially assume is 'high card' hand
        self.hand = 'HighCard'
        for method in self.tests:
            res = getattr(self,method)()
            if res:
                self.value = res
                self.hand = method[2:]
                break

    def __gt__(self,other):
        return self.value > other.value

    def getHandValues(self,hand):
        return list('0123456789TJQKA'.index(card) for card in [c[0] for c in hand])

    def isFlush(self):
        return len(set(self.suits)) == 1  and (5,self.ranks)
        
    def isStraight(self):
        high = self.ranks[0]
        return len(set(self.ranks))==5 and high - min(self.ranks) == 4 and (4,high)  # (4,highcard)

    def isStraightFlush(self):
        return self.isFlush() and self.isStraight() and (8,[self.ranks[0]]) # (8, highcard)

    def isRoyalFlush(self): 
       return self.isFlush() and self.ranks == [10,11,12,13,14]  and (9,)

    def ofAKind(self,n):
        counts = set((self.ranks.count(v),v) for v in self.ranks)
        res = []
        for c,v in counts:
            if c == n:
                res.append(v)
        return res 

    def isPair(self):
        res = self.ofAKind(2)
        return res and (1,res,self.ranks)
                
    def isFourOfAKind(self):
        res =  self.ofAKind(4)
        return res and (7,res,self.ranks)

    def isThreeOfAKind(self):
        res = self.ofAKind(3)
        return res and (3,res,self.ranks)

    def isTwoPair(self):
        res = self.ofAKind(2)
        return res and len(res) == 2 and (2,res,self.ranks)

    def isFullHouse(self):
        res3 = self.ofAKind(3)
        res2 = self.ofAKind(2)
        if res3 and res2 and res3 != res2:
            return (6,res3,res2)
        return False

def solve():
    count = 0
    for line in open('lib/poker.txt','r'):
        line = line.strip().split()
        if line:
            hand1,hand2 = Hand(line[:5]),Hand(line[5:])
            if hand1 > hand2:
                count += 1

    return count

if __name__ == '__main__':
    from lib.timer import best_time
    print(best_time(solve))


