#!/bin/bash

hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-3.3.6.jar \
    -input /user/hadoop/input/input.txt \
    -output /user/hadoop/output_new \
    -mapper /Users/mammadovzulfugar/Documents/ADA_University/Big_Data/homework_1/mapper.py \
    -reducer /Users/mammadovzulfugar/Documents/ADA_University/Big_Data/homework_1/reducer.py \
    -combiner /Users/mammadovzulfugar/Documents/ADA_University/Big_Data/homework_1/reducer.py \
    -file /Users/mammadovzulfugar/Documents/ADA_University/Big_Data/homework_1/mapper.py \
    -file /Users/mammadovzulfugar/Documents/ADA_University/Big_Data/homework_1/reducer.py;
