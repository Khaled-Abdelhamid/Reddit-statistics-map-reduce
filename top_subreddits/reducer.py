#!/usr/bin/python3

import sys
# Get the sorted subreddits and only get the top 100
NUMBER_OF_SUBREDDITS=100
count = 0

for line in sys.stdin:
    if count < NUMBER_OF_SUBREDDITS:
        _,subreddit,freq = line.split()
        print(subreddit,freq, sep='\t')
        count+=1
    else:
        pass