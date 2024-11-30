#Andres Lopez
#CS 106 Section 009
#HW 01, September 19, 2024

#5b
Age = 18
Semester = 1
Classes = 5
print(Age, Semester, Classes)

#5c
print()

Goal_GPA = 3.7
Pi = 3.141592
Flt= 9.643
print(Goal_GPA, Pi, Flt)

#5d
print()
last_firstname = 'Lopez, Andres'
favorite_color = 'orange'
major = 'Business'
print(last_firstname, favorite_color, major)

#6 

#1.1

#1. The console says unmatched ) and that there is a syntax error.

#2. The syntax error this time read unterminated string literal.

#3. It still adds the number normally and you would get back 4.

#4. It does not work in python and says leading zeros in decimal
#integer literals are not permitted and to use an 0o prefix for octal integers.

#5. The syntax error would say invalid syntax.

#1.2

#1.
print()
x = 42*60
x + 42
print(x)

#2.
print()
z = 10/1.61
print(z)

#3.
print()
y = x/3600 
print(z/y) 

#2.1

#1. It is not possible since I can't assign to the integer.

#2. It does allow x = y = 1

#3. Nothing happens to the code and it continues running as normally.

#4. The console returns invalid syntax and does not perform the code.

#5. It does not work and treats is treated as an undefined variable.

#2.2
import math

#1.
print()
print(4/3*math.pi*5**3)

#2.
print()
bkstrprce = 24.95 * 0.60
shpcst = 59 * 0.75
print(shpcst + 60*bkstrprce + 3)

#3.
print()
esypce = 2*0.0825
fstpce = 3*0.072

tmeran = esypce + fstpce

breakfast = 6.87 + tmeran
breakfast = '7:15'
print(breakfast)
