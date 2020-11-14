#!/usr/bin/python3

# sort all the values in decsending order 
import sys

# the big number is to make sure that the smaller number is higher in list (descending)
BIG_NUMBER=999999999999999999

for line in sys.stdin:
        subreddit, freq= line.split()
        order=str(BIG_NUMBER-int(freq))
        print(order, subreddit ,freq, sep='\t')
