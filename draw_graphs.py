"""
Matplotlib graph drawing
"""
import time
import random
import matplotlib.pyplot as plt
from shortest_path import a_star

matrix = []

a_star_running_time = []
dijkstra_running_tume = []

MAX_SIZE = 100


for i in range(2, MAX_SIZE+1):
    print(">>>", i)
    for _ in range(i):
        matrix.append( [ random.randint(1, 10000) for _ in range(i) ] )
    start = time.time()
    a_star(
        start_point=(0,0),
        end_point=(i-1, i-1),
        height_matrix=matrix,
        step=1
    )
    end = time.time()
    a_star_time = end - start
    a_star_running_time.append(a_star_time)
    matrix.clear()

line = plt.plot(range(2, MAX_SIZE+1), a_star_running_time)
line[0].set_label('A*')
plt.xlabel("Number of elements")
plt.ylabel("Running time")
plt.legend()
plt.show()
