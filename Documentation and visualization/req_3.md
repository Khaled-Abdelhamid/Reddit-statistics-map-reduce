[TOC]

# Algorithm

1. we need to print each word and the ups of its comment and the down votes of its comment
2. sum all ups and downs of a certain word
3. find the top 10 topics/words

## First map-reduce : get total ups and downs of a certain topic summed

* This map-reduce job is used to calculate the sum of ups and downs of each word in all comments
* the outout looks like that "Topic      sum_of_all_ups     sum_of_all_downs"


### Observations
Something weird in this dataset is that it contained 0 comments having posititve downvotes :''D

## Second map-reduce : Get the top `x` topics.

* This map-reduce job is used to get the top topics

### Observations
* due to lack of proper processing on the body some topics didn't make sense like "getting" it is a verb not a topic but the processing counted it as a topic

