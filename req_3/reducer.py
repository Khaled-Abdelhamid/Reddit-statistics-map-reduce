#!/usr/bin/python3
import sys

words = sys.stdin.readline().strip().split()
current = words[0]
up_sum = int(words[1])
down_sum = int(words[2])

for line in sys.stdin:
    words = line.strip().split()

    if words[0] == current:
        up_sum += int(words[1])
        down_sum += int(words[2])
    else:
        print(current, up_sum, down_sum, sep="\t")
        current = words[0]
        up_sum = int(words[1])
        down_sum = int(words[2])
