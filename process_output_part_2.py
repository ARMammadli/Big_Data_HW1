#!/Users/mammadovzulfugar/Documents/ADA_University/Big_Data/homework_1/.env/bin/python3
import sys
from collections import Counter
from tabulate import tabulate

def process_output(file_path):
    word_counts = Counter()

    # Open the file and read each line
    with open(file_path, 'r') as f:
        for line in f:
            word, count = line.strip().split('\t')
            word_counts[word] += int(count)

    # Total number of words
    total_word_count = sum(word_counts.values())

    # Top 10 most frequent words
    top_10_words = word_counts.most_common(10)

    # Number of unique words
    unique_word_count = len(word_counts)

    # Print results in a structured table format
    print("Word Count Summary\n")
    summary_table = [
        ["Total Number of Words", total_word_count],
        ["Number of Unique Words", unique_word_count]
    ]
    print(tabulate(summary_table, headers=["Statistic", "Value"], tablefmt="grid"))

    print("\nTop 10 Most Frequent Words\n")
    print(tabulate(top_10_words, headers=["Word", "Count"], tablefmt="grid"))


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python process_output.py <path_to_output_file>")
        sys.exit(1)

    output_file = sys.argv[1]
    process_output(output_file)
