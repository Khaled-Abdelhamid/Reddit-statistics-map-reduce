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
echo "                         getting topics frequency"
echo "============================================================================"
./get_topics_frequency.sh

echo "============================================================================"
echo "                           getting top topics"
echo "============================================================================"
./get_top_x_topics.sh