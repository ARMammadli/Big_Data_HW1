#!/bin/bash

# Run the Hadoop job for stopword removal and word count with a combiner
hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-3.3.6.jar \
    -input /user/hadoop/input/input.txt \
    -output /user/hadoop/output_stopwords \
    -mapper /Users/mammadovzulfugar/Documents/ADA_University/Big_Data/homework_1/mapper_stopword_removal.py \
    -reducer /Users/mammadovzulfugar/Documents/ADA_University/Big_Data/homework_1/reducer.py \
    -combiner /Users/mammadovzulfugar/Documents/ADA_University/Big_Data/homework_1/reducer.py \
    -file /Users/mammadovzulfugar/Documents/ADA_University/Big_Data/homework_1/mapper_stopword_removal.py \
    -file /Users/mammadovzulfugar/Documents/ADA_University/Big_Data/homework_1/reducer.py \
    -file /Users/mammadovzulfugar/Documents/ADA_University/Big_Data/homework_1/stopword_list.txt
