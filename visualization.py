"""
Visualization for graph as a heatmap
"""

import turtle

def visualization(matrix : list[list]) -> None:
    """
    Visualizes matrix.
    >>> visualization([[1, 14, 15, 234], [23, 34, 5, 5]])
    """

    tt = turtle.Turtle()
    tt.speed("fastest")
    tt.hideturtle()

    rows = len(matrix)
    columns = len(matrix[0])

    height_lst = []
    _ = [height_lst.extend(row) for row in matrix]
    height_lst = sorted(set(height_lst))

    colours = []
    for num,_ in enumerate(height_lst):
        colours.append((1/len(height_lst) * num,1/len(height_lst) * (len(height_lst) - num),1/len(height_lst) * num))

    if (max_pr := max(rows, columns)) <= 500:
        size = 50
    else:
        size = 25000 / max_pr
    print(size)
    h_col_dct = dict(zip(height_lst, colours))
    width = columns * size +250
    height = max(rows * size, 40 * (len(h_col_dct) + 1))
    turtle.screensize(width, height)

    tt.up()

    for row in range(rows):
        tt.goto(- width/2, height/2 - size * row)
        tt.down()
        for column in range(columns):
            tt.fillcolor(h_col_dct[matrix[row][column]])
            tt.begin_fill()
            for _ in range(4):
                tt.forward(size)
                tt.right(90)
            tt.forward(size)
            tt.end_fill()
        tt.up()

    tt.goto(size * columns - width/2 + 10, height/2 - 15)
    tt.write("The height in meters", align="left", font=("TimesNewRoman", 12, "bold"))

    tt.goto(size * columns - width/2 + 10 + 40, height/2 - 25 - 20)
    tt.write(f"{height_lst[0]}m.", align="left", font=("TimesNewRoman", 8, "normal"))

    for row in range(len(h_col_dct)):
        tt.goto(size * columns - width/2 + 10, height/2 -25 - (5 * row))
        tt.down()
        tt.fillcolor(colours[row])
        tt.begin_fill()
        tt.pencolor(colours[row])
        for _ in range(2):
            tt.forward(30)
            tt.right(90)
            tt.forward(5)
            tt.right(90)
        # tt.pencolor("black")
        tt.end_fill()
        tt.up()
    tt.pencolor("black")
    tt.goto(size * columns - width/2 + 10 + 40, height/2 - 25 - (5 * len(colours)))
    tt.write(f"{height_lst[-1]}m.", align="left", font=("TimesNewRoman", 8, "normal"))

    turtle.done()

if __name__ == "__main__":
    import doctest
    doctest.testmod()
