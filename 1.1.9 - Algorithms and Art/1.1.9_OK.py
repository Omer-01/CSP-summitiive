import turtle as trtl

painter = trtl.Turtle()

painter.pensize(5)
painter.pencolor("black")

my_list = ["red", "blue", "gray", "purple", "light green", "yellow", "orange"]
item_to_check = input == my_list

if item_to_check not in my_list:
    print(f"'{item_to_check}' is not in the list.")
else:
    print(f"'{item_to_check}' is in the list.")
# ---------------------

# draw house body
painter.setheading(45)

painter.goto(20,0)
painter.pendown()
painter.circle(100,360,4)
painter.penup()

painter.setheading(45)

painter.goto(160,0)
painter.pendown()
painter.circle(100,360,4)
painter.penup()


# draw house roof
painter.setheading(90)
painter.goto(160,140)
painter.pendown()

painter.circle(140,180,3)
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
painter.setheading(45)

painter.goto(1,0)
painter.pendown()
painter.circle(50,360,4)
painter.penup()

# draw house garage door
painter.setheading(45)

painter.goto(145,0)
painter.pendown()
painter.circle(80,360,4)
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