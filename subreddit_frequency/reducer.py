#!/usr/bin/python3

import sys
# sum all the values associated with keys to get the score of each subreddit
word = None
count = 0

for line in sys.stdin:
    key, value = line.strip().split()
    if word is None: # runs first time the only in the loop
        word = key
    elif word != key:# if the key changes then push the line in the output and reset to get another key
        print(word, count, sep='\t')
        word = key
        count = 0
    count += int(value)

print(word, count, sep='\t')
