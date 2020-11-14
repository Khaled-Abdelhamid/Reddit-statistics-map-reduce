#!/usr/bin/python3
import json
import sys

counter = 0
edited_count = 0
# sum all counts coming from different mappers
# sum all edited counts coming from different mappers
for line in sys.stdin:
    counts = line.strip().split()
    counter += int(counts[0])
    edited_count += int(counts[1])

# print unedited count and edited count
print(counter - edited_count, edited_count, sep="\t")
