from turtle import *
from time import *
bh , mh , sh = 200 , 170 , 120
bhc, mhc, shc = "green" , "red" , "blue"

def hand(angle,th,colorh):
  pencolor(colorh)
  a = (angle*-6)+90
  penup()
  goto(0,0)
  setheading(a)
  pendown()
  fd(th)


def cHand(angle,th):
  pencolor("white")
  b = (angle*-6)+90
  penup()
  goto(0,0)
  setheading(b)
  pendown()
  fd(th)
  penup()
  goto(0,0)
  pendown()
  pencolor("black")
  dot(10)



goto(0,0)
penup()
setheading(-90)
forward(240)
setheading(0)
pendown()
circle(240)
penup()
goto(0,0)
pendown()
dot(10)
penup()
delay(0)
speed(1000)
for i in range(0,360,30):
  pencolor("red")
  goto(0,0)
  setheading(i)
  penup()
  fd(220)
  pendown()
  fd(20)
  penup()

for min in range(60):
  hand(min,mh,mhc)
  for sec in range(60):
    hand(sec,bh,bhc)
    sleep(1)
    cHand(sec,bh)
    if min == sec: 
      hand(min,mh,mhc)
  cHand(min,mh)
    
