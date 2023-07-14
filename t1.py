from turtle import *

speed('normal')
pencolor('red')
#range(stop)
#range(start,stop)
#range(start,stop,step)

for i in range(6,40,5):
    fd(120)
    lt(360/10)
    dot(20,'blue')
    write(i,font=('Calibri',20,'bold'))
#reverse
goto(100,100)
for i in range(10,0,-1):
    fd(60)
    lt(360/10)
    dot(20,'red')
    write(i,font=('Calibiri',20,'bold'))



mainloop()