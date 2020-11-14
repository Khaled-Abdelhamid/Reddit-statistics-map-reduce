#!/usr/bin/python3

import sys
# sum all the values associated with keys to get the score of each subreddit
word = None
count = 0
upvotes=0
downvotes=0

for line in sys.stdin:
    username, value,ups,downs = line.strip().split()
    if word is None: # runs first time the only in the loop
        word = username
    elif word != username:# if the username changes then push the line in the output and reset to get another username
        print(word, count,upvotes,downvotes, sep='\t')
        word = username
        count = 0
        upvotes=0
        downvotes=0
    count += int(value)
    upvotes += int(ups)
    downvotes += int(downs)
    
print(word, count,upvotes,downvotes, sep='\t')
