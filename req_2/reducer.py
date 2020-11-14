#!/usr/bin/python3
import json
import sys


current = ""
c = "m"
count = 0
i = 0


# sum all parent ids and find its controversiality
# and print all three in one line "id    number_replies   controversiality"

for line in sys.stdin:
    data = line.strip().split()
    # check if the line id is the same as the last line (to keep counting)
    if data[0] == current:
        if len(data) == 2:
            count += 1
        if len(data) == 3:
            c = data[2]
    else:
        # if a new id is encountered set the count to 1 and/or controversiality(if available)
        # the if else is just to not print the very first line
        if i == 0:
            i = 1
            count = 1
            if len(data) == 3:
                c = data[2]
            current = data[0]
        else:
            print(current, count, c, sep="\t")
            if len(data) == 3:
                c = data[2]
            count = 1
            current = data[0]
