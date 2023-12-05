"""
Shortest path between 2 points on the surface problem
member1 = <Zhuk Maksym>
member2 = <Basystyi Oleh>
member3 = <Rudish Artur>
member4 = <Popeniuk Sofia>
member5 = <Marych Maksym>
GitHub repo: github.com/n1n1n1q/Shortest-Path-On-Surface
"""
import heapq

class PriorityQueue:
    """
    Implemetation of priority queue class.
    """
    def __init__(self):
        """
        Queue's initialization
        """
        self.elements = []

    def empty(self):
        """
        Empties the queue
        """
        return len(self.elements) == 0

    def put(self, item, priority):
        """
        Puts the element into the queue
        """
        heapq.heappush(self.elements, (priority, item))

    def get(self):
        """
        Gets queue's last element
        """
        return heapq.heappop(self.elements)[1]

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
    Finds distance between 2 neighbour points
    >>> get_distance((0, 0), (0, 1), [[1, 14, 15, 234], [23, 34, 5, 5]], 1)
    13.038404810405298
    >>> get_distance((0, 0), (0, 1), [[5,2],[1,2]],4)
    5.0
    """
    distance = height_matrx[start_point[0]][start_point[1]]-height_matrx[end_point[0]][end_point[1]]
    distance = (step ** 2 + distance ** 2) ** 0.5
    return distance

def get_neighbours(point: (int, int),matrix: list[list])-> list[tuple]:
    """
    Gets point's neighbours
    >>> get_neighbours((1,1),[[1,1,1,1],[1,1,1,1]])
    [(1, 2), (0, 1), (1, 0)]
    """
    neighbours=[]
    coordinates_delta=[1,-1]
    for i in range(2):
        if 0<=point[0]+coordinates_delta[i] < len(matrix):
            neighbours.append((point[0]+coordinates_delta[i], point[1]))
        if 0<=point[1]+coordinates_delta[i] < len(matrix[0]):
            neighbours.append((point[0],point[1]+coordinates_delta[i]))
    return neighbours

def is_valid(point: (int,int), matrix: list[list])-> bool:
    """
    Check if given point is valid
    >>> is_valid((10,10),[[1,1],[2,3]])
    False
    """
    return 0<=point[0]<len(matrix) and 0<=point[1]<len(matrix[0])

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
    >>> a_star((0,0), (2,1), [[1,1,1,1],[1000,1000,100,1],[1,1,1,1]],1)
    [(0, 0), (0, 1), (0, 2), (0, 3), (1, 3), (2, 3), (2, 2), (2, 1)]
    """
    if not is_valid(start_point,height_matrix) or not is_valid(end_point,height_matrix):
        return -1
    open_set = PriorityQueue()
    open_set.put(start_point, 0)
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

if __name__=='__main__':
    import doctest
    print(f'DOCTETS\
\n==================================\
            \n{doctest.testmod()}\
\n==================================\n')
    import time
    start_time=time.time()
    data=read_file('data.txt')
    print(f"Reading file finished; ~ time = {time.time()-start_time}")
    start_p,end_p,st=(0,0),(2,1),1
    print(f"Start point = {start_p}, end point = {end_p}, step = {st}")
    astar_start_time=time.time()
    a_star_output=a_star(start_point=start_p,end_point=end_p,height_matrix=data,step=st)
    print(f"Finished calculatin distance; ~ time = {time.time()-astar_start_time}")
    print(f"Shortest path = {a_star_output}\nTotal time: {time.time()-start_time}")
