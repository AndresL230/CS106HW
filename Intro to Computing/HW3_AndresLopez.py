#Andres Lopez
#CS 106 009
#HW 03, September 27, 2024

import turtle

turtle_canvas = turtle.Screen()
andres = turtle.Turtle()
andres.color('orange')

#1.

for i in range(3):
    andres.forward(100)
    andres.right(120)

andres.up()
andres.forward(200)
andres.down()

for i in range(4):
    andres.forward(100)
    andres.right(90)

andres.up()
andres.right(90)
andres.forward(200)
andres.down()

for i in range(5):
    andres.forward(100)
    andres.right(72)

#2.
andres.up()
andres.right(90)
andres.forward(350)
andres.right(90)
andres.forward(350)
andres.down()

andres.circle(50)
andres.right(90)
andres.up()
andres.forward(50)
andres.left(90)
andres.down()
andres.circle(100)
andres.right(90)
andres.up()
andres.forward(50)
andres.left(90)
andres.down()
andres.circle(150)
andres.right(90)
andres.up()
andres.forward(50)
andres.left(90)
andres.down()
andres.circle(200)

#3.
import math

factorial = math.factorial(100)
print(factorial)

print()

log = math.log(1000000, 2)
print(log)

print()

gcd = math.gcd(63, 49)
print(gcd)
