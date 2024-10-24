#!/bin/bash

# Run the Hadoop job for bigram counting with a combiner and stopword removal
hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-3.3.6.jar \
    -input /user/hadoop/input/input.txt \
    -output /user/hadoop/output_bigrams_stopwords \
    -mapper /Users/mammadovzulfugar/Documents/ADA_University/Big_Data/homework_1/mapper_bigrams.py \
    -reducer /Users/mammadovzulfugar/Documents/ADA_University/Big_Data/homework_1/reducer.py \
    -combiner /Users/mammadovzulfugar/Documents/ADA_University/Big_Data/homework_1/reducer.py \
    -file /Users/mammadovzulfugar/Documents/ADA_University/Big_Data/homework_1/mapper_bigrams.py \
    -file /Users/mammadovzulfugar/Documents/ADA_University/Big_Data/homework_1/reducer.py \
    -file /Users/mammadovzulfugar/Documents/ADA_University/Big_Data/homework_1/stopword_list.txt

