#!/usr/bin/python3

import sys
from heapq import heappush, heappushpop
# variables to keep track of tag, flag and top X topics
NUM_OF_TOPICS=10

heap = []
current_tag = None
current_flag = None

for line in sys.stdin:
        flag_tag,topic,score = line.strip().split()
        score=int(score)
        flag,tag =flag_tag.split(sep=":")
        # intial values for the flag and tag
        if current_tag==None:current_tag=tag
        if current_flag==None:current_flag=flag
        # if any of them changed reset everything again
        if  current_tag!=tag or current_flag!=flag:
                top_topics = sorted(heap, reverse=True) 
                top_topics=[str(element) for element in top_topics]
                formatted_top_topics="-".join(top_topics)
                
                print(f"{current_flag}:{current_tag}",formatted_top_topics,sep='\t')
                current_flag=flag
                current_tag=tag
                heap=[]
        # fill the heap till it reachs max topics then replace the minimum
        if len(heap) < NUM_OF_TOPICS:
                heappush(heap, (score,topic))
        else:
                heappushpop(heap, (score,topic))

top_topics = sorted(heap, reverse=True) 
top_topics=[str(element) for element in top_topics]
formatted_top_topics="".join(top_topics)
print(f"{current_flag}:{current_tag}",formatted_top_topics,sep='\t')


# data="Most of us have some family members like 5 6 5656 this. *Most* of my family is like this. But Mill's career was way better. Bentham is like, the Joseph Smith to Mill's Brigham Young."
# res=Preprocess_Body(data)
# print(res)
# print(len(res))

# print(len(subreddits))
