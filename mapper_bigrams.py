#!/Users/mammadovzulfugar/Documents/ADA_University/Big_Data/homework_1/.env/bin/python3
import sys
import re

# Load stopwords from file
stopwords = set()
with open('stopword_list.txt', 'r') as f:
    for line in f:
        stopwords.add(line.strip().lower())

# Regular expression to remove punctuation
pattern = re.compile(r'[^\w\s]')

# Process each line from standard input
for line in sys.stdin:
    line = line.strip()
    # Remove punctuation and split into words
    words = pattern.sub('', line).split()
    # Convert to lowercase, filter out stopwords and empty strings
    filtered_words = [word.lower() for word in words if word and word.lower() not in stopwords]

    # Generate bigrams and emit them if there are at least two words
    for i in range(len(filtered_words) - 1):
        bigram = f"{filtered_words[i]} {filtered_words[i + 1]}"
        print(f"{bigram}\t1")
