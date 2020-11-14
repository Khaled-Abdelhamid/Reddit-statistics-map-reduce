[TOC]

# Algorithm
1. A counter that holds the number of all comments and a number that holds the number the count of all edited comments
2. sum all comments and edited comments coming from different mappers
3. print all counters

## one map-reduce needed
* This map job is used to print the count of all the comments and the edited comments in that map task
* The reduce sums counts coming from different map tasks


### Observations
Most of the comments are not edited

