import turtle
t = turtle.Turtle()
t.right(90)
t.forward(50)
t.right(90)
t.circle(50)

t.left(90)
t.forward(20)
t.right(90)
t.circle(30)

t.left(90)
t.forward(20)
t.right(90)
for i in range(30):
    t.circle(10-(i/3))
t.left(90)
t.forward(10)
t.right(90)
t.forward(100)
t.left(180)
t.forward(200)
t.left(180)
t.forward(100)
t.left(90)
t.forward(100)


turtle.done()