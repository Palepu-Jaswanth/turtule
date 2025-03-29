import turtle as t
import colorsys
t.bgcolor("black")
t.tracer(100)
t.pensize(1)
h=0.5
for i in range(350):
    c=colorsys.hsv_to_rgb(h,1,1)
    h=0.0008
    t.fillcolor(c)
    t.begin_fill()
    t.fd(i)
    t.circle(50)
    for j in range(2):
        t.fd(i*j)
        t.rt(100)
        t.end_fill()
