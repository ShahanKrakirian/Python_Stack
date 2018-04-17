# Coin Tosses 
# .50 rounds to 1, .49 rounds to 0

import random 

def coin_tosses(number_of_tosses):
    heads = 0
    tails = 0
    for i in range(0, number_of_tosses):
        x = round(random.random())
        if x == 1.0:
            heads += 1
            print "Attempt #", i, "Throwing a coin... It's a head! ... Got", heads, "head(s) so far and", tails, "tail(s) so far."
        else: 
            tails += 1
            print "Attempt #", i, "Throwing a coin... It's a tail! ... Got", heads, "head(s) so far and", tails, "tail(s) so far."

coin_tosses(5000)