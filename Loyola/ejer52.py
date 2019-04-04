import turtle

cali = []
for i in range(4):
    cali.insert(i, int(input(f'ingrese la calificacion {i+1}: ')))

t = turtle.Turtle()
for i in range(4):
    t.pendown()
    t.left(90)
    t.forward(cali[i]*5)
    t.right(90)
    t.forward(30)
    t.right(90)
    t.forward(cali[i]*5)
    t.right(90)
    t.forward(30)
    t.penup()
    t.left(180)
    t.forward(50)
turtle.done()