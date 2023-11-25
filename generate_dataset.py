import random 

ROWS = 1000
COLS = 1000
MAX_HEIGHT = 10000

with open('data.txt', 'w') as data_file:
    for i in range(0, ROWS):
        data_file.write(' '.join( [ str(random.randint(1, MAX_HEIGHT)) for i in range(COLS) ] ) + '\n')
