#myfunctions.py


import turtle
bob = turtle.Turtle()
from random import randint

def human():
    for times in range(432):
         bob.circle(times * 10000)
         bob.forward(times * 5)
         bob.left(120)

def jump(x, y):
    bob.penup
    bob.goto(x, y)
    bob.pendown()

def neo():
    for times in range(82):
        bob.forward(6)
        bob.right(6)
        bob.circle(20)


def neomax():
    for times in range (5):
        neo()
        x = randint(-300,300)
        y = randint(-300, 300)
        jump(x, y)
        
def jay():
    for times in range(4):
        bob.color("red")
        bob.forward(100)
        bob.left(90)
        x = randint(-300,300)
        y = randint(-300, 300)
        jump(x, y)
        
        
  
    

    
   
   
   

