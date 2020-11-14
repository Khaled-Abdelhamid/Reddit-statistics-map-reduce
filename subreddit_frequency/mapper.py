#!/usr/bin/python3

import sys
import json
# parse the line as json dictionary and print the subreddit as a key with weight equal to its upvotes + downvotes (high interaction)
for line in sys.stdin:
        content=json.loads(line)
        # print(content['subreddit'], abs(content['ups'])+abs(content['downs']), sep='\t')
        print(content['subreddit'], 1, sep='\t')