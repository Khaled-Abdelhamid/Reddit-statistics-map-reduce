#!/usr/bin/python3
import json
import sys


current = ""
c = "m"
count = 0
i = 0

for line in sys.stdin:
    data = line.strip().split()
    if data[0] == current:
        if len(data) == 2:
            count += 1
        if len(data) == 3:
            c = data[2]
    else:
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
