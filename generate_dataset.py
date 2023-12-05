"""
Generates random data sets for the problem
"""
import random

ROWS = 5000
COLS = 5000
MAX_HEIGHT = 10000

with open('data.txt', 'w', encoding='utf-8') as data_file:
    for i in range(0, ROWS):
        data_file.write(' '.join( [ str(random.randint(1, MAX_HEIGHT))\
                                    for _ in range(COLS) ] ) + '\n')
print("DATA GENERATION FINISHED")
