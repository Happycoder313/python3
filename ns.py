import turtle

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

# Hide the turtle after drawing
tonny.hideturtle()

# Keep the window open until clicked
screen.exitonclick()
