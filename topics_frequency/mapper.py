#!/usr/bin/python3

import sys
import string
import re
import json
import logging


# subreddits=["AskReddit","CFB","funny","pcmasterrace","hockey","pics","leagueoflegends","nfl","nba","AdviceAnimal","video","WT","worldnew","todayilearne","gamin","new","DestinyTheGam","anim","movie","GlobalOffensiv","serialpodcas","xboxon","DotA","SquaredCircl","atheis","TumblrInActio","tree","explainlikeimfiv","soccer"]

stop_words = ('yes','would','dont','im','also','one','like','ourselves', 'hers', 'between', 'yourself', 'but', 'again', 'there', 'about', 'once', 'during', 'out', 'very', 'having', 'with', 'they', 'own', 'an', 'be', 'some', 'for', 'do', 'its', 'yours', 'such', 'into', 'of', 'most', 'itself', 'other', 'off', 'is', 's', 'am', 'or', 'who', 'as', 'from', 'him', 'each', 'the', 'themselves', 'until', 'below', 'are', 'we', 'these', 'your', 'his', 'through', 'don', 'nor', 'me', 'were', 'her', 'more', 'himself', 'this', 'down', 'should', 'our', 'their', 'while', 'above', 'both', 'up', 'to', 'ours', 'had', 'she', 'all', 'no', 'when', 'at', 'any', 'before', 'them', 'same', 'and', 'been', 'have', 'in', 'will', 'on', 'does', 'yourselves', 'then', 'that', 'because', 'what', 'over', 'why', 'so', 'can', 'did', 'not', 'now', 'under', 'he', 'you', 'herself', 'has', 'just', 'where', 'too', 'only', 'myself', 'which', 'those', 'i', 'after', 'few', 'whom', 't', 'being', 'if', 'theirs', 'my', 'against', 'a', 'by', 'doing', 'it', 'how', 'further', 'was', 'here', 'than')
def Preprocess_Body(body:str)->set:        
        result=body.lower()
        result=result.translate(str.maketrans('', '', string.punctuation))
        result = set(re.sub(r'\d+', '', result).split())
        result = [word for word in result if word not in stop_words ]
        return result
def score(content:dict)->int:
        return 1
subreddits=[]
with open("part-00000") as fp: 
        logging.info("file read successfully")
        Lines = fp.readlines() 
        for line in Lines: 
                subreddit,_=line.split()
                subreddits.append(subreddit)

for line in sys.stdin:
        content=json.loads(line)
        if content['subreddit'] in subreddits:
                topics=Preprocess_Body(content['body'])          
                for topic in topics:
                        print(f"u:{content['author']}:{topic}", score(content), sep='\t')
                        print(f"r:{content['subreddit']}:{topic}", score(content), sep='\t')



# data="Most of us have some family members like 5 6 5656 this. *Most* of my family is like this. But Mill's career was way better. Bentham is like, the Joseph Smith to Mill's Brigham Young."
# res=Preprocess_Body(data)
# print(res)
# print(len(res))

# print(len(subreddits))
