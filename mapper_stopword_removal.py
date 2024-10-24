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
    for word in words:
        word = word.lower()
        # Emit word count if word is not a stopword
        if word not in stopwords and word != '':
            print(f"{word}\t1")
