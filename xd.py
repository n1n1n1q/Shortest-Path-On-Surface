def get_neighbours(point: (int, int),matrix: list[list])-> list[tuple]:
    """
    
    """
    neighbours=[]
    coordinates_delta=[1,-1]
    for i in range(2):
        if point[0]+coordinates_delta[i] in range(0,len(matrix)):
            neighbours.append((point[0]+coordinates_delta[i], point[1]))
        if point[1]+coordinates_delta[i] in range(0, len(matrix[0])):
            neighbours.append((point[0],point[1]+coordinates_delta[i]))
    return neighbours

print(get_neighbours((1,1),[[1, 14, 15, 234], [23, 34, 5, 5]]))