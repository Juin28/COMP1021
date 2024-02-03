import random
import turtle

turtle.speed(8)
turtle.shape("turtle")

colorlist = ["red","orange","yellow","green","blue","indigo","purple","pink","gold","silver","cyan","brown"]

i = 0

while i <= 200:
    x = random.randint(-400,400)
    y = random.randint(-300,300)
    l = random.randint(10,100)
    w = random.randint(10,100)
    t = random.randint(0,360)
    h = random.randint(1,15)
    lc = random.choice(colorlist)
    fc = random.choice(colorlist)
    turtle.begin_fill()
    turtle.color(lc,fc)
    turtle.up()
    turtle.goto(x,y)
    turtle.down()
    turtle.width(h)
    turtle.left(t)
    turtle.forward(l)
    turtle.left(90)
    turtle.forward(w)
    turtle.left(90)
    turtle.forward(l)
    turtle.left(90)
    turtle.forward(w)
    turtle.end_fill()
    i += 1
