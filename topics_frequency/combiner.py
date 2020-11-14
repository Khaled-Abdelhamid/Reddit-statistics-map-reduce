#!/usr/bin/python3

import sys

current_tag = None
current_topic = None
current_flag = None
sum = 0

for line in sys.stdin:
    id_topic, score = line.strip().split()
    score=int(score)
    flag,tag,topic =id_topic.split(sep=":")
    
    if current_tag==None:current_tag=tag
    if current_topic==None:current_topic=topic
    if current_flag==None:current_flag=flag
    
    if current_topic!=topic or current_tag!=tag or current_flag!=flag:
        print(f"{current_flag}:{current_tag}:{current_topic}",sum,sep='\t')
        sum=0
        current_flag=flag
        current_topic=topic
        current_tag=tag
    sum+=score
    
print(f"{current_flag}:{current_tag}:{current_topic}",sum,sep='\t')
