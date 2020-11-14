#!/usr/bin/python3
import sys


# do the same process as the mapper but on the output of all mappers

x = 10

top_ups = [["", -1] for _ in range(x)]
top_downs = [["", -1] for _ in range(x)]


def sort_second(val):
    return val[1]


for line in sys.stdin:
    words = line.strip().split()
    # direction is either "ups" or "downs"
    direction = words[0]
    word = words[1]

    # if ups and the sum is bigger than the last topic in the list then replace it and resort
    if direction == "ups":
        up_sum = int(words[2])
        if up_sum > top_ups[-1][1]:
            top_ups[-1][0] = word
            top_ups[-1][1] = up_sum
            top_ups.sort(key=sort_second, reverse=True)

    # if downs and the sum is bigger than the last topic in the list then replace it and resort
    if direction == "downs":
        down_sum = int(words[2])
        if down_sum > top_downs[-1][1]:
            top_downs[-1][0] = word
            top_downs[-1][1] = down_sum
            top_downs.sort(key=sort_second, reverse=True)

# print top x topics but this time will be global max over all the topics not the mapper
for i in range(x):
    print("ups", top_ups[i][0], top_ups[i][1], sep="\t")
for i in range(x):
    print("downs", top_downs[i][0], top_downs[i][1], sep="\t")
