import turtle
import random

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("white")

# Create the turtle object
tonny = turtle.Turtle()
tonny.shape("turtle")
tonny.speed(3)

# Function to draw a circle with a specific color and radius
def draw_circle(color, radius, x, y):
    tonny.penup()
    tonny.goto(x, y)
    tonny.pendown()
    tonny.begin_fill()
    tonny.fillcolor(color)
    tonny.circle(radius)
    tonny.end_fill()

# Function to draw the face
def draw_face():
    # Draw face (main circle)
    draw_circle("yellow", 100, 0, -100)

    # Draw eyes (two smaller circles)
    draw_circle("white", 15, -35, 0)  # Left eye
    draw_circle("white", 15, 35, 0)   # Right eye

    # Draw pupils (smaller black circles inside the eyes)
    draw_circle("black", 7, -35, 10)  # Left pupil
    draw_circle("black", 7, 35, 10)   # Right pupil

    # Draw a nose (small circle)
    draw_circle("orange", 10, 0, -30)

    # Draw a smile (arc)
    tonny.penup()
    tonny.goto(-40, -40)
    tonny.setheading(-60)
    tonny.pendown()
    tonny.circle(50, 120)

# Function to make eyes blink
def blink_eyes():
    tonny.penup()
    tonny.goto(-35, 0)
    tonny.pendown()
    tonny.color("white")
    tonny.begin_fill()
    tonny.circle(15)
    tonny.end_fill()

    tonny.penup()
    tonny.goto(35, 0)
    tonny.pendown()
    tonny.color("white")
    tonny.begin_fill()
    tonny.circle(15)
    tonny.end_fill()

    tonny.color("black")
    tonny.penup()
    tonny.goto(-35, 10)
    tonny.pendown()
    tonny.begin_fill()
    tonny.circle(7)
    tonny.end_fill()

    tonny.penup()
    tonny.goto(35, 10)
    tonny.pendown()
    tonny.begin_fill()
    tonny.circle(7)
    tonny.end_fill()

# Function to change eye color
def change_eye_color():
    colors = ["blue", "green", "brown", "purple", "black"]
    eye_color = random.choice(colors)
    
    # Redraw the face and eyes with new eye color
    draw_face()
    tonny.penup()
    tonny.goto(-35, 10)
    tonny.pendown()
    tonny.color(eye_color)
    tonny.begin_fill()
    tonny.circle(7)
    tonny.end_fill()

    tonny.penup()
    tonny.goto(35, 10)
    tonny.pendown()
    tonny.color(eye_color)
    tonny.begin_fill()
    tonny.circle(7)
    tonny.end_fill()

# Draw initial face
draw_face()

# Make the eyes blink
blink_eyes()

# Change the eye color after some time
screen.ontimer(change_eye_color, 2000)  # Change eye color after 2 seconds

# Keep the window open until clicked
screen.exitonclick()
