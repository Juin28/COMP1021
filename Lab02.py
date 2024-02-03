# COMP1021 Lab 2 Python Sketchbook
# Name: Tan Juin
# Student ID: 20913887
# Email: jtanat@connect.ust.hk

import turtle       # Import the turtle module for the program

turtle.width(4)
turtle.speed(10)

##### Initialize the colour
fillcolor = "black"
turtle.pencolor("black")
turtle.fillcolor(fillcolor)
turtle.begin_fill()

print("Welcome to the Python Sketchbook!")

##### While loop to repeat the main menu

# Initialize the option to empty in order to enter the while loop
option = ""


while option != "q": # While the option is not "q"
    print()
    print("Please choose one of the following options:")
    print()
    print("m - Move the turtle")
    print("t - Rotate the turtle")
    print("l - Draw a line")
    print("r - Draw a rectangle")
    print("c - Draw a circle")
    print("p - Change the pen colour of the turtle")
    print("f - Change the fill colour of the turtle")
    print("g - Draw a generated flower")
    print("e - Draw a generated explosion")
    print("a - Draw the author's information")
    print("q - Quit the program")
    print()

    option = input("Please enter your option: ")

    ##### Handle the move option
    if option == "m":
        print()

        # Ask the user for the x and y value
        x = input("Please enter the x value: ")
        x = int(x)
        y = input("Please enter the y value: ")
        y = int(y)

        # Move the turtle without drawing anything
        turtle.up()
        turtle.goto(x, y)
        turtle.down()

    ##### Handle the rotate option
    if option == "t":
        print()

        # Please put your code here
        angle = input("Please enter the angle of rotation: ")
        angle = int(angle)
        turtle.left(angle)

    ##### Handle the line option
    if option == "l":
        print()

        # Ask the user for the x and y value
        x = input("Please enter the x value: ")
        x = int(x)
        y = input("Please enter the y value: ")
        y = int(y)

        # Move the turtle and draw a line
        turtle.goto(x, y)

    ##### Handle the rectangle option
    if option == "r":
        print()

        # Please put your code here
        w = input("Please enter the width  of the rectangle: ")
        w = int(w)
        h = input("Please enter the height of the rectangle: ")
        h = int(h)
        turtle.begin_fill()
        for _ in range(2):
            turtle.forward(w)
            turtle.left(90)
            turtle.forward(h)
            turtle.left(90)
        turtle.end_fill()

    ##### Handle the circle option
    if option == "c":
        print()

        # Please put your code here
        r = input("Please enter the radius of the circle: ")
        r = int(r)
        turtle.begin_fill()
        turtle.circle(r)
        turtle.end_fill()

    ##### Handle the pen colour option
    if option == "p":
        print()

        # Please put your code here
        pen_color = input("Please enter a colour name for the pen colour: ")
        turtle.pencolor(pen_color)
        
    ##### Handle the fill colour option
    if option == "f":
        print()

        # Please put your code here
        fill_color = input("Please enter a colour name for the fill colour :")
        turtle.fillcolor(fill_color)

    if option == "g":
        print()

        petal_size = input("Please enter the size of the flower petal: ")
        petal_size = int(petal_size)
        for num in range(12):
            for tri in range(3):
                turtle.forward(petal_size)
                turtle.left(120)
            turtle.left(360/12)

    if option == "e":
        print()

        explosion_type = input("Please enter the type of generated explosion (one colour or multiple colours): ")
        
        if explosion_type == "one colour":
            explosion_size = input("Please enter the size of the explosion (>150): ")
            explosion_size = int(explosion_size)
            explosion_size1 = explosion_size
            for dot_color in ["sienna", "brown", "red", "dark orange", "orange","gold2", "gold", "yellow"]:
                turtle.pencolor(dot_color)
                turtle.dot(explosion_size1)
                explosion_size1 = explosion_size1 - explosion_size/7

        if explosion_type == "multiple colours":
            explosion_size = input("Please enter the size of the explosion (>160): ")
            explosion_size = int(explosion_size)
            explosion_size1 = explosion_size
            for outer_dot_color in ["turquoise","brown","DarkOrange","yellow"]:
                for inner_dot in range(4):
                    inner_dot = inner_dot + 1
                    inner_dot_color = outer_dot_color + str(inner_dot)
                    turtle.pencolor(inner_dot_color)
                    turtle.dot(explosion_size1)
                    explosion_size1 = explosion_size1 - explosion_size/16

        turtle.pencolor(pen_color)

    if option == "a":
        print()
        turtle.up()
        turtle.goto(-200,200)
        
        for j_up in range(4):
            turtle.dot(30)
            turtle.forward(30)
        turtle.right(90)
        for j_mid in range(6):
            turtle.dot(30)
            turtle.forward(30)
        turtle.right(90)
        turtle.forward(30)
        for j_bot in range(3):
            turtle.dot(30)
            turtle.forward(30)
        turtle.right(90)
        turtle.forward(30)
        turtle.dot(30)

        turtle.goto(-20,200)

        turtle.left(180)
        
        for u_le in range(5):
            turtle.dot(30)
            turtle.forward(30)
        turtle.left(90)
        turtle.forward(30)
        turtle.dot(30)
        turtle.forward(30)
        turtle.right(90)
        turtle.forward(30)
        turtle.left(90)
        for u_mid in range(2):
            turtle.dot(30)
            turtle.forward(30)
        turtle.left(90)
        turtle.forward(30)
        turtle.dot(30)
        turtle.forward(30)
        turtle.right(90)
        turtle.forward(30)
        turtle.left(90)
        for u_rig in range(5):
            turtle.dot(30)
            turtle.forward(30)
        
        turtle.goto(190,200)
        turtle.left(180)
        
        for i in range(7):
            turtle.dot(30)
            turtle.forward(30)

        turtle.goto(250,200)

        for n_le in range(7):
            turtle.dot(30)
            turtle.forward(30)
        turtle.goto(250,200)
        for n_mid in range(6):
            turtle.forward(30)
            turtle.left(90)
            turtle.forward(30)
            turtle.dot(30)
            turtle.right(90)
        turtle.right(180)
        for n_rig in range(7):
            turtle.dot(30)
            turtle.forward(30)


turtle.done()
