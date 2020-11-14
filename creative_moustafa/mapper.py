#!/usr/bin/python3
import json
import sys

# count of all comments
counter = 0

# count of edited comments only
edited_count = 0

for line in sys.stdin:
    data = json.loads(line)
    edited = data["edited"]
    counter += 1
    if edited:
        edited_count += 1

print(counter, edited_count, sep="\t")
