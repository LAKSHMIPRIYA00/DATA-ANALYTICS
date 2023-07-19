from turtle import*
speed('fastest')
colors=['red','white','green','blue']
pensize(2)
for i in range(100):
    #print(i%4,color[i%4])
    pencolor(colors[i%4])
    fd(i*2)
    lt(60)
    circle(i*2,270)
mainloop()