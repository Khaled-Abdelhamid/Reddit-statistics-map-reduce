#!/usr/bin/python3

import sys
# Get the sorted usernames and only get the top 100
NUMBER_OF_USERS=200
count = 0

for line in sys.stdin:
    if count < NUMBER_OF_USERS:
        order,username,freq,ups,downs = line.split()
        # score=str(int(freq)+abs(int(ups))+abs(int(downs)))
        print(username,freq,ups,downs, sep='\t')
        count+=1
    else:
        pass