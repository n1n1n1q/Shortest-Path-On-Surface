def get_distance(start_point: (int, int), 
                        end_point: (int, int),
                        height_matrx: list[list], 
                        step: int)-> list[list]:
    """
    >>> get_distance((0, 0), (1, 2), [[1, 14, 15, 234], [23, 34, 5, 5]], 2)
    inf
    >>> get_distance((0, 0), (0, 1), [[1, 14, 15, 234], [23, 34, 5, 5]], 2)
    13.152946437965905
    """
    if start_point[0] == end_point[0] and abs(start_point[1] - end_point[1]) == 1:
        distance = height_matrx[start_point[0]][start_point[1]] - height_matrx[end_point[0]][end_point[1]]
        return (step ** 2 + distance ** 2) ** 0.5
    if start_point[1] == end_point[1] and abs(start_point[0] - end_point[0]) == 1:
        distance = height_matrx[start_point[0]][start_point[1]] - height_matrx[end_point[0]][end_point[1]]
        return (step ** 2 + distance ** 2) ** 0.5
    return float("inf")

if __name__=='__main__':
    import doctest
    print(doctest.testmod())
    