
import turtle
t = turtle.Turtle()
t.speed(0)

# letra A
# t.left(90)
# t.circle(-4.5, 180)
# t.forward(13)

# t.left(90)
# t.forward(0.9)

# t.right(180)
# t.forward(5)
# t.circle(-4, 180)
# t.forward(8)

# letra B
# t.right(90)
# t.forward(20)
# t.left(90)
# t.forward(5)
# t.circle(5, 180)
# t.forward(5)
#letra C
# t.left(180)
# t.forward(3)
# t.circle(-6, 180)
# t.forward(3)
#letra d
# t.right(90)
# t.forward(20)
# t.right(90)
# t.forward(5)
# t.circle(-5, 180)
# t.forward(5)


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

t.penup()
t.left(180)
t.forward(135)
t.left(90)
t.forward(5)
t.pendown()
# letra A
t.right(90)
t.circle(-4.5, 180)
t.forward(13)

t.left(90)
t.forward(0.9)

t.right(180)
t.forward(5)
t.circle(-4, 180)
t.forward(8)

t.penup()
t.forward(16)
t.right(90)
t.forward(15)
t.pendown()
# letra B
#t.right(90)
t.forward(20)
t.left(90)
t.forward(5)
t.circle(5, 180)
t.forward(5)

t.penup()
t.left(90)
t.forward(39)
t.right(90)
t.forward(19)
t.pendown()
#letra C
t.forward(5)
t.circle(-6, 180)
t.forward(5)

t.penup()
t.left(90)
t.forward(35)
t.left(90)
t.forward(30)
t.pendown()

#letra d
t.left(90)
t.forward(20)
t.right(90)
t.forward(5)
t.circle(-5, 180)
t.forward(5)
t.penup()
t.forward(100)
turtle.done()

