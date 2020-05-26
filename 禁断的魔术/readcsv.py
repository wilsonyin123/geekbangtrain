import pandas as pd


filename = 'book.csv'
with open(filename, "r", encoding='utf-8') as f:
    for line in f:
        print(line)

