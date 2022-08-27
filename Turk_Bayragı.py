from turtle import *
title("Türk Bayrağı")
setup(width=600, height=400)
bgcolor("red")
hideturtle()

def renk_ve_konum(renk,x,y):
    penup()
    goto(x,y)
    pendown()
    color(renk)
    begin_fill()

def yildiz():
    renk_ve_konum("white",80,25)

    for i in range(5):
        forward(50)
        right(144)
        forward(50)
        right(-72)
    end_fill()

def ay(cap):
    circle(cap)
    end_fill()

renk_ve_konum("white",-110,-120)
ay(130)
renk_ve_konum("red",-70,-90)
ay(100)
yildiz()

mainloop()