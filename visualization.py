"""
Algorithm's visualization via turtle
"""
import turtle
from random import randint
rows = 4
columns = 4
size = 75

tt = turtle.Turtle()
tt.speed("fastest")

tt.up()

colours = [(0.8, 0.9, 1),(0.68, 0.85, 0.9), (0, 0, 0.8), (0, 0, 0.5), (0, 0, 0.6), (0, 0, 0.2)]
height_lst = [0, 100, 200, 300, 400, 500]

for row in range(rows):
    tt.goto(-200, 150 - size * row)
    tt.down()
    for _ in range(columns):
        tt.fillcolor(colours[randint(0, 5)])
        tt.begin_fill()
        for _ in range(4):
            tt.forward(size)
            tt.right(90)
        tt.forward(size)
        tt.end_fill()
    tt.up()

tt.goto(size * columns - 200 + 50, 150)
tt.write("The height in meters", align="left", font=("TimesNewRoman", 12, "bold"))

for row in range(6):
    tt.goto(size * columns - 200 + 50, 150 - 10 - (35 * row))
    tt.down()
    tt.fillcolor(colours[row])
    tt.begin_fill()
    for _ in range(4):
        tt.forward(30)
        tt.right(90)
    tt.end_fill()
    tt.up()
    tt.goto(size * columns - 200 + 50 + 40, 150 - 10 - 30 - (35 * row))
    tt.write(f"{height_lst[row]}m.", align="left", font=("TimesNewRoman", 12, "normal"))

turtle.done()
