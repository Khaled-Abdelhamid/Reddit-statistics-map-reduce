[TOC]


# Algorithm

1. print parent_id of each comment and print the controversiality of an id once 
2. count parent_id count (to know how many replies for that parent_id comment)
3. output "parent_id    count_of_replies    controversiality"


## one map-reduce needed
### Mapper
* mapper outputs the controversiality of a comment once and outputs parent_id
* build dictionary to check if the current id controversiality was streamed before or not

### Reducer
* sum all parent ids and find its controversiality
* and print all three in one line "id    number_replies   controversiality"


### Observations
* All ids in the dataset had controversiality = 0 which is weird  also all comments had 0 downvotes so it is a biased dataset


