#!/bin/bash
echo "============================================================================"
echo "                       getting subreddit frequency"
echo "============================================================================"
./get_subreddit_freq.sh

echo "============================================================================"
echo "                         getting top subreddits"
echo "============================================================================"
./get_top_x_subreddits.sh

echo "============================================================================"
echo "                       getting users frequency"
echo "============================================================================"
./get_users_freq.sh

echo "============================================================================"
echo "                         getting top users"
echo "============================================================================"
./get_top_x_users.sh

echo "============================================================================"
echo "                         getting topics frequency"
echo "============================================================================"
./get_topics_frequency.sh

echo "============================================================================"
echo "                           getting top topics"
echo "============================================================================"
./get_top_x_topics.sh

# echo "============================================================================"
# echo "                           rate of replies compared to controversiality"
# echo "============================================================================"
# ./rate.sh

# echo "============================================================================"
# echo "                           All topics ups and downs"
# echo "============================================================================"
# ./all_topics_ups_downs.sh

# echo "============================================================================"
# echo "                           Top topics ups and downs"
# echo "============================================================================"
# ./top_topics_ups_downs.sh

# echo "============================================================================"
# echo "                            Count of Non-edited vs Edited"
# echo "============================================================================"
# ./creative_mo.sh


