#!/bin/bash

export JAVA_HOME=/usr/lib/jvm/java-1.8.0-openjdk/
export HADOOP_HOME=/hadoop
export PATH=${JAVA_HOME}/bin:${HADOOP_HOME}/bin:${PATH}
export HADOOP_CLASSPATH=${JAVA_HOME}/lib/tools.jar:${HADOOP_HOME}/share/hadoop/tools/lib/*

code="top_x_topics"
input="output/topics_frequency"
input_file="part-*"
mappers=5
reducers=1

hadoop fs -rm -r $code
yes | rm -r output/$code
yes |hadoop fs -rm -r output/$code

hadoop fs -rm -r $input

echo Uploading data to hdfs ...
hadoop fs -mkdir -p $code
hadoop fs -put $code/* $code

hadoop fs -mkdir -p $input
hadoop fs -put $input/$input_file $input

hadoop org.apache.hadoop.streaming.HadoopStreaming -D mapred.map.tasks=$mappers -D mapred.reduce.tasks=$reducers\
    -files $code/mapper.py,$code/reducer.py \
    -input $input/$input_file \
    -output output/$code \
    -mapper mapper.py \
    -reducer reducer.py

hadoop fs -get output/$code output/$code
