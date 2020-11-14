#!/usr/bin/python3
import json
import sys

lookup_table = {}
for line in sys.stdin:
    data = json.loads(line)
    parent_id = data["parent_id"]
    current_id = data["link_id"]
    if current_id not in lookup_table:
        lookup_table[current_id] = 1
        print(current_id, "c", data["controversiality"], sep="\t")
    print(parent_id, 1, sep="\t")
