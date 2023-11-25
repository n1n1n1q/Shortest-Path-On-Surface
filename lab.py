"""

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
    >>> read_file('data.txt')
    [[1, 14, 15, 234], [23, 34, 5, 5]]
    """
    raw_data = []
    with open(filename,'r',encoding='utf-8') as file:
        raw_data = [ [ int(height) for height in line.strip().split()]
                      for line in file.readlines()  ]
    #print(raw_data)
    return raw_data




def A_star():
    

if __name__=='__main__':
    import doctest
    print(doctest.testmod())
