#!/usr/bin/python3

import sys
# variables to check if any of the flags,topics or tags has changed
current_tag = None
current_topic = None
current_flag = None
sum = 0

for line in sys.stdin:
    # parse the vaues coming from mapper
    flag_tag_topic, score = line.strip().split()
    score=int(score)
    flag,tag,topic =flag_tag_topic.split(sep=":")
    # sets the current variables intially if they weren't set 
    if current_tag==None:current_tag=tag
    if current_topic==None:current_topic=topic
    if current_flag==None:current_flag=flag
    
    #if the flag , tag or tpoic changed , reset the variables and output the the last total score to the stream
    if current_topic!=topic or current_tag!=tag or current_flag!=flag:
        print(f"{current_flag}:{current_tag}",current_topic,sum,sep='\t')
        sum=0
        current_flag=flag
        current_topic=topic 
        current_tag=tag
    sum+=score
    
print(f"{current_flag}:{current_tag}",current_topic,sum,sep='\t')
