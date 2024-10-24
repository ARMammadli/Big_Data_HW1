#!/Users/mammadovzulfugar/Documents/ADA_University/Big_Data/homework_1/.env/bin/python3
import sys

current_word = None
current_count = 0
for line in sys.stdin:
    word, count = line.split("\t")
    count = int(count)
    if current_word == word:
        current_count += count
    else:
        if current_word:
            print(f"{current_word}\t{current_count}")
        current_word = word
        current_count = count

if current_word == word:
    print(f"{current_word}\t{current_count}")
