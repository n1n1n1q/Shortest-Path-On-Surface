"""
lab2
"""
from queue import PriorityQueue

def read_file(filename: str)-> list[list]:
    """
    Reads graph from file and transforms it into a matrix.
    >>> import tempfile
    >>> with tempfile.NamedTemporaryFile('w', delete=False) as tmp:
    ...     _=tmp.write('1 14 15 234\\n23 34 5 5')
    >>> read_file(tmp.name)
    [[1, 14, 15, 234], [23, 34, 5, 5]]
    """
    raw_data = []
    with open(filename,'r',encoding='utf-8') as file:
        raw_data = [ [ int(height) for height in line.strip().split()]
                      for line in file.readlines()  ]
    return raw_data

def get_distance(start_point: (int, int), 
                        end_point: (int, int),
                        height_matrx: list[list], 
                        step: int)-> list[list]:
    """
    >>> get_distance((0, 0), (1, 2), [[1, 14, 15, 234], [23, 34, 5, 5]], 2)
    inf
    >>> get_distance((0, 0), (0, 1), [[5,2],[1,2]],4)
    5.0
    """
    if start_point[0] == end_point[0] and abs(start_point[1] - end_point[1]) == 1:
        distance = height_matrx[start_point[0]][start_point[1]] \
            - height_matrx[end_point[0]][end_point[1]]
        return (step ** 2 + distance ** 2) ** 0.5
    if start_point[1] == end_point[1] and abs(start_point[0] \
                                              - end_point[0]) == 1:
        distance = height_matrx[start_point[0]][start_point[1]] \
            - height_matrx[end_point[0]][end_point[1]]
        return (step ** 2 + distance ** 2) ** 0.5
    return float('inf')
    # return (step ** 2 + distance ** 2) ** 0.5 if end_point in\
    # get_neighbours(start_point,height_matrx) else float("inf")

def get_neighbours(point: (int, int),matrix: list[list])-> list[tuple]:
    """
    Gets point's neighbours
    >>> get_neighbours((1,1),[[1,1,1,1],[1,1,1,1]])
    [(1, 2), (0, 1), (1, 0)]
    """
    neighbours=[]
    coordinates_delta=[1,-1]
    for i in range(2):
        if point[0]+coordinates_delta[i] in range(0,len(matrix)):
            neighbours.append((point[0]+coordinates_delta[i], point[1]))
        if point[1]+coordinates_delta[i] in range(0, len(matrix[0])):
            neighbours.append((point[0],point[1]+coordinates_delta[i]))
    return neighbours

def is_valid(point: (int,int), matrix: list[list])-> bool:
    """
    Check if given point is valid
    >>> is_valid((10,10),[[1,1],[2,3]])
    False
    """
    return point[0] in range(0,len(matrix)) and point[1] in range(0,len(matrix[0]))

def heuristic(start_point: (int, int), end_point: (int, int)) -> int:
    """
    Calculates distance between indexes
    >>> heuristic((0, 5), (10, 3))
    12
    """
    return abs(start_point[0] - end_point[0] ) + abs(start_point[1] - end_point[1])


def reconstruct_path(came_from: dict, current: (int, int)):
    """
    Recreates path to the point
    """
    total_path = [current]
    while current in came_from.keys():
        current = came_from[current]
        if current:
            total_path.insert(0, current)
    return total_path


def a_star(start_point: (int,int),
           end_point: (int,int),
           height_matrix: list[list[int]],
           step: int)-> float:
    """
    A star algorithms

    """
    if not is_valid(start_point,height_matrix) or not is_valid(end_point,height_matrix):
        return -1
    open_set = PriorityQueue()
    open_set.put(start_point)
    came_from = {}
    cost = {}

    came_from[start_point] = None
    cost[start_point] = 0

    while not open_set.empty():
        current = open_set.get()

        if current == end_point:
            return reconstruct_path(came_from, current)

        for next_point in get_neighbours(current, height_matrix):
            new_cost = cost[current] + get_distance(start_point=current,
                                                    end_point=next_point,
                                                    height_matrx=height_matrix,
                                                    step=step)
            if next_point not in cost or new_cost < cost[next_point]:
                cost[next_point] = new_cost
                priority = new_cost + heuristic(end_point, next_point)
                open_set.put(next_point, priority)
                came_from[next_point] = current

    return -1

# if __name__=='__main__':
    # import doctest
    # print(doctest.testmod())
    # import time
    # from random import randint
    # height_matrix = read_file("data.txt")
    
    # def print_rand_elem(matrix):
    #     print(matrix[0][1])
    
    # func_total=0
    # no_func_total=0
    # for i in range(250000000):
    #     t=time.time()
    #     print_rand_elem(height_matrix)
    #     t=time.time()-t
    #     func_total+=t
    #     print(f"func time = {t}")
    #     t=time.time()
    #     print(height_matrix[0][1])
    #     t=time.time()-t
    #     no_func_total+=t
    #     print(f"no func time ={t} ")
    # print(f"{func_total=},{no_func_total}")
    # print(f"readfile time = {time.time()-t}")
    # t=time.time()
    # start = (0, 0)
    # end = (3000, 3000)
    # a_star(start_point=start, end_point=end, height_matrix=height_matrix, step=1)
    # print(f"a_star time  = {time.time()-t}")
