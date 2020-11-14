#!/usr/bin/python3

import sys
# parse the files and send them to sort and reduce
for line in sys.stdin:
        flag_tag,topic,score = line.strip().split()
        print(flag_tag,topic,score,sep='\t')

