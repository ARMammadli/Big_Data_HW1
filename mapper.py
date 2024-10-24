#!/Users/mammadovzulfugar/Documents/ADA_University/Big_Data/homework_1/.env/bin/python3
import sys
import re

pattern = re.compile(r'[^\w\s]')
for line in sys.stdin:
    line = line.strip().lower()
    words = pattern.sub('', line).split()
    for word in words:

        print(f"{word}\t1")

