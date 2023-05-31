import csv
import random


def csv_file():
    with open('save_file.csv', 'w', newline='') as f:
        for _ in range(random.randint(100, 1000)):
            csv.writer(f).writerow([random.randint(1, 10), random.randint(1, 10), random.randint(1, 10)])


csv_file()
