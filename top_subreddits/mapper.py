#!/usr/bin/python3

import sys
import json

BIG_NUMBER=9999999999999

for line in sys.stdin:
        subreddit, freq= line.split()
        order=str(BIG_NUMBER-int(freq))
        print(order, subreddit ,freq, sep='\t')
