#!/bin/bash

export JAVA_HOME=/usr/lib/jvm/java-1.8.0-openjdk/
export HADOOP_HOME=/hadoop
export PATH=${JAVA_HOME}/bin:${HADOOP_HOME}/bin:${PATH}
export HADOOP_CLASSPATH=${JAVA_HOME}/lib/tools.jar:${HADOOP_HOME}/share/hadoop/tools/lib/*

code="creative_moustafa"
input="input"
input_file="big6"
mappers=5
reducers=1

hadoop fs -rm -r $code
yes | rm -r output/$code
yes |hadoop fs -rm -r output/$code
yes |hadoop fs -rm -r top_subreddits

hadoop fs -rm -r $input

echo Uploading data to hdfs ...
hadoop fs -mkdir -p $code
hadoop fs -put $code/* $code

hadoop fs -mkdir -p $input
hadoop fs -put $input/$input_file $input

# hadoop fs -mkdir -p top_subreddits
# hadoop fs -put output/top_subreddits/* top_subreddits

hadoop org.apache.hadoop.streaming.HadoopStreaming -D mapred.map.tasks=$mappers -D mapred.reduce.tasks=$reducers\
    -files $code/mapper.py,$code/reducer.py,output/top_subreddits/part-00000 \
    -input $input/$input_file \
    -output output/$code \
    -mapper mapper.py \
    -reducer reducer.py

hadoop fs -get output/$code output/$code
