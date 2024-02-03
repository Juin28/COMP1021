import random
import turtle

target = random.randint(1,100)
finished = False
count = 0
xposition = -100
yposition = 150

turtle.up()

turtle.goto(xposition,yposition)
turtle.write("I am thinking of a number. What number am I thinking off?"
             , font=("Arial", 15, "bold"))
yposition = yposition - 40

while not finished:
    guess_input_text = turtle.textinput("Guessing Game",
                                        "Please enter a number between 1 and 100: ")
    guess_input = int(guess_input_text)
    count = count + 1
    if guess_input < 1 or guess_input > 100:
        turtle.goto(xposition,yposition)
        turtle.write("Please enter an integer number between 1 and 100."
                     , font=("Arial", 15, "bold"))
        yposition = yposition - 40
    elif guess_input > target:
        turtle.goto(xposition, yposition)
        turtle.write("Too high."
                     , font=("Arial", 15, "bold"))
        yposition = yposition - 40
    elif guess_input < target:
        turtle.goto(xposition, yposition)
        turtle.write("Too low."
                     , font=("Arial", 15, "bold"))
        yposition = yposition - 40
    else:
        finished = True

turtle.goto(xposition, yposition)
turtle.write("You got it! My number is " + str(target)
             , font=("Arial", 15, "bold"))
yposition = yposition - 40
turtle.goto(xposition, yposition)
turtle.write("It took you " + str(count) + " guesses to get the number!"
             , font=("Arial", 15, "bold"))
yposition = yposition - 40
    
turtle.done()
