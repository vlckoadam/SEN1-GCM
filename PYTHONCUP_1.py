import turtle
import random
turtle = turtle.Turtle()

def obdlznik(a,b):
    turtle.forward(a) 
    turtle.left(90)    
    
    turtle.forward(b) 
    turtle.left(90)
    
    turtle.forward(a) 
    turtle.left(90) 
        
    turtle.forward(b) 
    turtle.left(90) 

def slnko(n, strana, luc):
    for _ in range(n):
        turtle.forward(strana)
        turtle.right(360 / n)
        obdlznik(strana, luc)

x = random.randint(-350,300+1)
y = random.randint(100,220+1)
n = random.randint(5,15+1)
strana = random.randint(10,20+1)
luc = random.randint(30,80+1)


turtle.penup()
turtle.goto(x,y)
turtle.pendown()

slnko(n, strana, luc)
