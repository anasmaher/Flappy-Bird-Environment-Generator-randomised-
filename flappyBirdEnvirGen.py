from turtle import *
import random

s = Screen()
t = Turtle()

s.setup(600 , 600)
s.bgcolor('black')
t.shape('turtle')
t.color("white",'dark red')

#constants

tunnelWidth = 50
headWidth = 110
headLen = 30

def f(dirc, ln, sp):
    t.up()
    t.rt(90 * dirc)
    t.goto(sp, 300*dirc)
    t.down()

    t.begin_fill()
    t.fd(ln)
    t.lt(90*dirc)
    t.fd(tunnelWidth)
    t.lt(90*dirc)
    t.fd(ln)
    t.end_fill()
    
    t.begin_fill()
    t.lt(180*dirc)
    t.fd(ln)
    t.lt(90*dirc)
    t.fd((headWidth - tunnelWidth) // 2)
    t.rt(90*dirc)
    t.fd(headLen)
    t.rt(90*dirc)
    t.fd(headWidth)
    t.rt(90*dirc)
    t.fd(headLen)
    t.rt(90*dirc)
    t.fd((headWidth - tunnelWidth) // 2)
    t.end_fill()
    
    
    
prvLn = 100
for i in range(10):
    ln = random.randint(prvLn, 450 - prvLn - 30 - 40)
    prvln = ln
    
    if i%2 == 0:
        f(1, ln, -270 + i*100)
    else:
        f(-1, ln, -270 + i*100)
     

done()



