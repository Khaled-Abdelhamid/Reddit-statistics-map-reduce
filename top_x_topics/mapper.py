#!/usr/bin/python3

import sys

for line in sys.stdin:
        flag_tag,topic,score = line.strip().split()
        score=int(score)
        print(flag_tag,topic,score,sep='\t')

