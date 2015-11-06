"""
Coin sums
Problem 31

In England the currency is made up of pound, £, and pence, p, and there are eight coins in general circulation:

        1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p).

        It is possible to make £2 in the following way:

        1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p

        How many different ways can £2 be made using any number of coins?

"""


def dynamic_solution():
    """
       =====================================================
        coins   1p  <=2p   <=3p    <=4p    <=5p    <=10p  ... 
       ===================================================== 
       ||goal|| 
       || 1  || 1     1     1        1       1       1      
       || 2  || 1     2     2        2       2       2
       || 3  || 1     2     2        2       2       2 
       || 4  || 1     3     3        3       3       3  
       || 5  || 1   
       || 6  || 1   
       || 7  || 1   
       ||... ||
       
       Some observations:
       The first column and first row will be all 1's. When you The pattern that emerges is 
       that goal x using <=n = [ goal x <=(n-1) ] + goal (x-n) using <=n.
       example:
            the ways to get a 4 using coins up to 2p or less is the number of ways 
            you can make a 4 using 1p or less + the number of ways you can make a 
            2 using 2p or less. This makes sense because when you add a coing you 
            are using all of the old ways that did not include that new coin and so
            any new combinations must include that new coin and so you are really concerned
            with how many ways you can close the gap between the new coin and the goal (x-n)
    """
    coins = (1, 2, 5, 10, 20, 50, 100, 200)
    Last_Coin = {coins[i]:coins[i-1] for i in range(1,len(coins))}
    # represent chart as a dictionary of dictionaries1
    # { goal: {coin: ways} }
    chart = {}
    # initialize chart
    for goal in range(201):
        chart[goal] = {1:1}
    for coin in coins:
        chart[1][coin] = 1
        chart[0][coin] = 1
    # build up chart 

    last = 1
    for goal in range(2,201):
        for coin in coins[1:]:
            if coin > goal:
                ways = last
            else:
                 ways = chart[goal][Last_Coin[coin]] + chart[goal-coin][coin]
            last = ways
            chart[goal][coin] = ways

    return chart[200][200]


def brute_force_solution():
    count = 0

    for P2 in range(0,201,200):
        if P2 >= 200:
            if P2 == 200:
                count += 1
            break
        for P1 in range(0,201,100):
            total =P2+P1 
            if total >= 200:
                if total == 200:
                    count += 1
                break
            for p50 in range(0,201,50):
                total =P2+P1+p50 
                if total  >= 200:
                    if total == 200:
                        count += 1
                    break
                for p20 in range(0,201,20):
                    total =P2+P1+p50+p20 
                    if total >= 200:
                        if total == 200:
                            count += 1
                        break
                    for p10 in range(0,201,10):
                        total = P2+P1+p50+p20+p10
                        if total >= 200:
                            if total == 200:
                                count += 1
                            break
                        for p5 in range(0,201,5):
                            total = P2+P1+p50+p20+p10+p5
                            if total >= 200:
                                if total == 200:
                                    count += 1
                                break
                            for p2 in range(0,201,2):
                                total = P2+P1+p50+p20+p10+p5+p2
                                if total >= 200:
                                    if total == 200:
                                        count += 1
                                    break
                                for p1 in range(0,201):
                                     total = P2+P1+p50+p20+p10+p5+p2+p1
                                     if total >= 200:
                                         if total == 200:
                                             count += 1
                                         break
                                   
    return count

solve = dynamic_solution

if __name__ == '__main__':
    from time import time
    t1 = time()
    print('brute force solution found {} in {:.5f} miliseconds'.format(brute_force_solution(),(time()-t1)*1000))
    t1 = time()
    print('dynamic solution found {} in {:.5f} miliseconds'.format(dynamic_solution(),(time()-t1)*1000))

    
