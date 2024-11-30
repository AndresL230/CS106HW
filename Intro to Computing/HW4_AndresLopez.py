#Andres Lopez
#CS 106 009
#HW 04, October 4, 2024

#1.
#a
a = 3
b = 4
c = 5

#b
if a < b:
    print('OK')

#c
if c < b:
    print('OK')
#d
if a+b == c:
    print('OK')

#e
if b**2 + a**2 == c**2:
    print('OK')

#2.
print()

if a < b:
    print('OK')
else:
    print('NOT OK')
    
if c < b:
    print('OK')
else:
    print('NOT OK')
    
if a+b == c:
    print('OK')
else:
    print('NOT OK')

if b**2 + a**2 == c**2:
    print('OK')
else:
    print('NOT OK')

#3.
print()

t_color = input('What Color? ')
t_width = input('What line width? ')
t_length = input('What line length? ')
t_shape = input('What shape, line, triangle, or square? ')

import turtle

output_screen = turtle.Screen()
output = turtle.Turtle()
output.color(t_color)
output.width(int(t_width))

if t_shape == ('line'):
    output.forward(int(t_length))

if t_shape == ('square'):
    output.forward(int(t_length))
    output.right(90)
    output.forward(int(t_length))
    output.right(90)
    output.forward(int(t_length))
    output.right(90)
    output.forward(int(t_length))
    output.right(90)
    
if t_shape == ('triangle'):
    output.forward(int(t_length))
    output.right(120)
    output.forward(int(t_length))
    output.right(120)
    output.forward(int(t_length))
    output.right(120)
