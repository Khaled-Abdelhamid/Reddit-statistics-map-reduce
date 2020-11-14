#!/usr/bin/python3
import sys

# define how many topics to output (top x)
x = 10

# create a list made up of 10 elements so that it continously keeps the top 10 topics and by the end of execution it has the global max topics (over the mapper)
top_ups = [["", -1] for _ in range(x)]
top_downs = [["", -1] for _ in range(x)]


# sorting criteria (sort by second element)
def sort_second(val):
    return val[1]


for line in sys.stdin:
    words = line.strip().split()
    word = words[0]
    up_sum = int(words[1])
    down_sum = int(words[2])

    # check if current topic up and down votes sum bigger than the last element of top_ups and top_downs which hold the sorted (current) top 10 topics
    # if bigger then replace the last topic of the list with the current topic
    if up_sum > top_ups[-1][1]:
        top_ups[-1][0] = word
        top_ups[-1][1] = up_sum
    if down_sum > top_downs[-1][1]:
        top_downs[-1][0] = word
        top_downs[-1][1] = down_sum

    # continously sort elements of top_ups and top_downs (so that always last topic in the list has the minimum sum)
    top_ups.sort(key=sort_second, reverse=True)
    top_downs.sort(key=sort_second, reverse=True)

# finally stream top x topics with ups and downs at begninning key so each category goes to one reducer (to get global max)

for i in range(x):
    print("ups", top_ups[i][0], top_ups[i][1], sep="\t")

for i in range(x):
    print("downs", top_downs[i][0], top_downs[i][1], sep="\t")
