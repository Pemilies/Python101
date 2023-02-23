import turtle
tao = turtle.Pen()
colors = ['red', 'purple', 'blue', 'green', 'orange', 'yellow']
turtle.bgcolor('black')
for x in range(50):
    tao.pencolor(colors[x%6])
    tao.circle(x*3)
    tao.left(10)
