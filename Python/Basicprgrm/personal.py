import turtle
import time

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Colorful Heart Animation")
screen.setup(width=600, height=600)

# Create turtle object
pen = turtle.Turtle()
pen.speed(0)
pen.width(2)

# Define heart shape
def heart():
    pen.color("red")
    pen.fillcolor("red")
    pen.begin_fill()
    pen.left(140)
    pen.forward(224)
    for _ in range(200):
        pen.right(1)
        pen.forward(2)
    pen.left(120)
    for _ in range(200):
        pen.right(1)
        pen.forward(2)
    pen.forward(224)
    pen.end_fill()

# Main animation loop
while True:
    pen.clear()
    pen.up()
    pen.goto(0, -100)
    pen.down()
    heart()
    pen.up()
    pen.goto(0, -200)
    pen.down()
    pen.color("cyan")
    pen.write("Happy Valentine's Day!", align="center", font=("Courier", 24, "normal"))
    time.sleep(2)  # Pause for 2 seconds
