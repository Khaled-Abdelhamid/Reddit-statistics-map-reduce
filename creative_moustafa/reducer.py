#!/usr/bin/python3
import json
import sys

counter = 0
edited_count = 0
for line in sys.stdin:
    counts = line.strip().split()
    counter += int(counts[0])
    edited_count += int(counts[1])

print(counter - edited_count, edited_count, sep="\t")
