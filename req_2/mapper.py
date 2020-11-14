#!/usr/bin/python3
import json
import sys

# mapper outputs the controversiality of a comment once and outputs parent_id

# dictionary to check if the current id controversiality was streamed before or not
lookup_table = {}
for line in sys.stdin:
    data = json.loads(line)
    parent_id = data["parent_id"]
    current_id = data["link_id"]
    if current_id not in lookup_table:
        lookup_table[current_id] = 1
        print(current_id, "c", data["controversiality"], sep="\t")

    # stream parent_id and 1 (to count how many replies for a comment)
    print(parent_id, 1, sep="\t")
