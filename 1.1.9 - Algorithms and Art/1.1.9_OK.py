import turtle as trtl

painter = trtl.Turtle()


# ---------------------
painter.pensize(5)
painter.pencolor("black")
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
painter.setheading(45)

painter.goto(-83,10)
painter.pendown()
painter.circle(20,360,4)
painter.penup()

painter.setheading(45)

painter.goto(-83,50)
painter.pendown()
painter.circle(20,360,4)
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
painter.setheading(45)

painter.goto(18,-85)
painter.pendown()
painter.circle(60,360,4)
painter.penup()

painter.setheading(45)

painter.goto(160,-140)
painter.pendown()
painter.circle(100,360,4)
painter.penup()

# ---------------------
wn = trtl.Screen()
wn.mainloop()