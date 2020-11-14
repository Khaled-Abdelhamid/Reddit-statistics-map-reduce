#!/usr/bin/python3

# sort all the values in decsending order 
import sys

# the big number is to make sure that the smaller number is higher in list (descending)
BIG_NUMBER=999999999999999999

for line in sys.stdin:
        username, freq,ups,downs= line.split()
        # order=str(BIG_NUMBER-int(freq)-abs(int(ups))-abs(int(downs)))
        order=str(BIG_NUMBER-int(freq))
        
        print(order, username ,freq,ups,downs ,sep='\t')
