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
# draw house windows


# draw house door


# draw house garage



# draw house driveway 



# ---------------------
wn = trtl.Screen()
wn.mainloop()