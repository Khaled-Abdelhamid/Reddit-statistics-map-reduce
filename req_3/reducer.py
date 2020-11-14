#!/usr/bin/python3
import sys

#  same as the combiner reads the line and just sums all the upvotes and downvotes for each word
# read the first line
words = sys.stdin.readline().strip().split()
current = words[0]
up_sum = int(words[1])
down_sum = int(words[2])

for line in sys.stdin:
    words = line.strip().split()

    # if word is the same as last line keep summing
    if words[0] == current:
        up_sum += int(words[1])
        down_sum += int(words[2])

    # else print and set the new word
    else:
        print(current, up_sum, down_sum, sep="\t")
        current = words[0]
        up_sum = int(words[1])
        down_sum = int(words[2])
