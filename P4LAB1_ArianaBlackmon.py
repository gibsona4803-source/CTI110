import turtle

# --- Setup the Screen and Turtle ---
screen = turtle.Screen()
screen.setup(width=600, height=600)
screen.bgcolor("hotpink")          # Changed background to Hot Pink
screen.title("Pink Turtle House Project")

artist = turtle.Turtle()
artist.shape("turtle")             
artist.color("deeppink")           # Changed turtle color to a contrasting dark pink
artist.pensize(3)
artist.speed(3)                    

# --- Step 1: Draw the Base of the House (Square) ---
# Using a FOR loop for the 4 sides of the square base.
artist.penup()
artist.goto(-100, -100)            
artist.pendown()

artist.begin_fill()
artist.fillcolor("lightpink")      # Changed house base to Light Pink

for _ in range(4):
    artist.forward(200)            
    artist.left(90)                

artist.end_fill()

# --- Step 2: Draw the Roof (Triangle) ---
# Moving to the top left corner of the square (-100, 100) to start the roof.
artist.penup()
artist.goto(-100, 100)
artist.pendown()

artist.begin_fill()
artist.fillcolor("purple")         # Purple roof looks great with hot/light pink!

# Using a WHILE loop for the 3 sides of the triangle roof.
sides_drawn = 0
while sides_drawn < 3:
    artist.forward(200)
    artist.left(120)               
    sides_drawn += 1

artist.end_fill()

# --- Step 3: Getting Creative (Adding a Door) ---
artist.penup()
artist.goto(-30, -100)             
artist.pendown()

artist.begin_fill()
artist.fillcolor("white")          # White door to contrast nicely with the light pink walls

for _ in range(2):
    artist.forward(60)
    artist.left(90)
    artist.forward(100)
    artist.left(90)

artist.end_fill()

# --- Step 4: Adding a Little Tree next to the house ---
artist.penup()
artist.goto(160, -100)
artist.pendown()

# Trunk
artist.begin_fill()
artist.fillcolor("darkviolet")
for _ in range(2):
    artist.forward(30)
    artist.left(90)
    artist.forward(60)
    artist.left(90)
artist.end_fill()

# Foliage
artist.penup()
artist.goto(145, -40)
artist.pendown()
artist.begin_fill()
artist.fillcolor("magenta")        # Magenta tree top to complete the theme
artist.circle(40)                  
artist.end_fill()

# --- Wrap Up ---
artist.hideturtle()                
screen.mainloop()