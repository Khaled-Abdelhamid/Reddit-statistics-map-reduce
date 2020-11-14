#!/usr/bin/python3

import sys

NUMBER_OF_TOPICS=30
count = 0

for line in sys.stdin:
    if count < NUMBER_OF_TOPICS:
        _,subreddit,freq = line.split()
        print(subreddit,freq, sep='\t')
        count+=1
    else:
        break