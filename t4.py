from turtle import*
speed('fastest')
pensize(2)
bgcolor('black')
pencolor('white')
color=['red','blue','pink','green','orange','purple']
side=9
for i in range(side):
    fd(200)
    for i in range(side):
        fd(100)
        lt(360/side)
        begin_fill()
        fillcolor(color[i%6])
        for i in range(side):
            fd(50)
            lt(360/side)
        end_fill()
    lt(360/side)

hideturtle()
mainloop()            