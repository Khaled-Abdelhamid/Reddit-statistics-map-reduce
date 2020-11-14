#!/usr/bin/python3

import sys
import string
import re
import json
import logging

stop_words = ('went','similar','k','truley','think','thanks','really','good','thats','deleted','get','yes','would','dont','im','also','one','like','ourselves', 'hers', 'between', 'yourself', 'but', 'again', 'there', 'about', 'once', 'during', 'out', 'very', 'having', 'with', 'they', 'own', 'an', 'be', 'some', 'for', 'do', 'its', 'yours', 'such', 'into', 'of', 'most', 'itself', 'other', 'off', 'is', 's', 'am', 'or', 'who', 'as', 'from', 'him', 'each', 'the', 'themselves', 'until', 'below', 'are', 'we', 'these', 'your', 'his', 'through', 'don', 'nor', 'me', 'were', 'her', 'more', 'himself', 'this', 'down', 'should', 'our', 'their', 'while', 'above', 'both', 'up', 'to', 'ours', 'had', 'she', 'all', 'no', 'when', 'at', 'any', 'before', 'them', 'same', 'and', 'been', 'have', 'in', 'will', 'on', 'does', 'yourselves', 'then', 'that', 'because', 'what', 'over', 'why', 'so', 'can', 'did', 'not', 'now', 'under', 'he', 'you', 'herself', 'has', 'just', 'where', 'too', 'only', 'myself', 'which', 'those', 'i', 'after', 'few', 'whom', 't', 'being', 'if', 'theirs', 'my', 'against', 'a', 'by', 'doing', 'it', 'how', 'further', 'was', 'here', 'than')
def Preprocess_Body(body:str)->set:
        """performs the following operations in the text to retrieve all the important topics 
        1- sets all words to lower case
        2- remove all punctuation from the string
        3- remove all of the digits
        4- remove all stop - unneccisary common words
        5- convert this to a set to get all unique values
        Args:
            body (str): [The main string to be preproccessed]

        Returns:
            set: [A set of topics in the body]
        """
        result=body.lower()
        result=result.translate(str.maketrans('', '', string.punctuation))
        result = re.sub(r'\d+', '', result).split()
        result = [word for word in result if word not in stop_words ]
        return set(result)
def score(content:dict)->int:
        """gets the score of each topic in the post

        Args:
            content (dict): passes the content information for the subreddit to be processed

        Returns:
            int: the output score for each post
        """
        return 1

# this is made to read and cahce the top subreddits aquired from the previous step
subreddits=[]
with open("top_subreddits") as fp: 
        Lines = fp.readlines() 
        for line in Lines: 
                subreddit,_=line.split()
                subreddits.append(subreddit)

users=[]
with open("top_users") as fp: 
        Lines = fp.readlines() 
        for line in Lines: 
                user,_,_,_=line.split()
                users.append(user)


for line in sys.stdin:
        content=json.loads(line)
        #check if the subreddit is in the top 100 or not
        if content['subreddit'] in subreddits and content['author'] in users:
                # for each post preprocess the body 
                topics=Preprocess_Body(content['body'])          
                for topic in topics:
                        #output the username with user flag (u) along with the the topic
                        print(f"u:{content['author']}:{topic}", score(content), sep='\t')
                        #output the subbreddit name subreddit flag(r) along with the the topic
                        print(f"r:{content['subreddit']}:{topic}", score(content), sep='\t')


## testing lines
# data="Most of us have some family members like 5 6 5656 this. *Most* of my family is like this. But Mill's career was way better. Bentham is like, the Joseph Smith to Mill's Brigham Young."
# res=Preprocess_Body(data)
# print(res)
# print(len(res))

# print(len(subreddits))
