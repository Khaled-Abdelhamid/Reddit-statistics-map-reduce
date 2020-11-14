#!/usr/bin/python3

import sys

NUMBER_OF_TOPICS=20
count = 0

for line in sys.stdin:
    if count < NUMBER_OF_TOPICS:
        order , subreddit , freq = line.split()
        print(order,subreddit,freq, sep='\t')
        count+=1
    else:
        break