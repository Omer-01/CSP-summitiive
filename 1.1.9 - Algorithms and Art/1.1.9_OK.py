import turtle as trtl

painter = trtl.Turtle()


painter.pensize(5)
painter.pencolor("black")

color_list = ["red", "blue", "green", "purple", "orange", "light blue"]
color_prompt = "Choose a color for the house from the following options:\n" + ", ".join(color_list)
house_color = ""

# Get user input for the house color, validating against the color list
while house_color.lower() not in color_list:
    house_color = trtl.textinput("House Color", color_prompt)
    if house_color is None: # Handle user canceling the input dialog
        exit()
    if house_color.lower() not in color_list:
        color_prompt = "Invalid color. Please choose one from the list:\n" + ", ".join(color_list)



# ---------------------

# draw house body
painter.fillcolor(house_color)
painter.setheading(45)

painter.goto(20,0)
painter.pendown()
painter.begin_fill()
painter.circle(100,360,4)
painter.end_fill()
painter.penup()

painter.setheading(45)

painter.goto(160,0)
painter.pendown()
painter.begin_fill()
painter.circle(100,360,4)
painter.end_fill()
painter.penup()


# draw house roof
painter.fillcolor("brown")
painter.setheading(90)
painter.goto(160,140)
painter.pendown()
painter.begin_fill()
painter.circle(140,180,3)
painter.end_fill()
painter.penup()
# draw house windows
painter.fillcolor("light blue")

painter.setheading(45)

painter.goto(-83,10)
painter.pendown()
painter.begin_fill()
painter.circle(20,360,4)
painter.end_fill()
painter.penup()

painter.setheading(45)

painter.goto(-83,50)
painter.pendown()
painter.begin_fill()
painter.circle(20,360,4)
painter.end_fill()
painter.penup()

# draw house front door
painter.fillcolor("light gray")
painter.setheading(45)

painter.goto(1,0)
painter.pendown()
painter.begin_fill()
painter.circle(50,360,4)
painter.end_fill()
painter.penup()

# draw house garage door
painter.fillcolor("light gray")
painter.setheading(45)

painter.goto(145,0)
painter.pendown()
painter.begin_fill()
painter.circle(80,360,4)
painter.end_fill()
painter.penup()


# draw house driveway 
painter.fillcolor("black")
painter.setheading(45)

painter.goto(18,-85)
painter.pendown()
painter.begin_fill()
painter.circle(60,360,4)
painter.penup()
painter.end_fill()
painter.setheading(45)

painter.goto(160,-140)
painter.pendown()
painter.begin_fill()
painter.circle(100,360,4)
painter.penup()
painter.end_fill()
# ---------------------
wn = trtl.Screen()
wn.mainloop()