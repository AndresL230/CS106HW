#Andres Lopez
#CS 106 009
#HW 05, October 13, 2024

#1.
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

for i in months:
    if 'J' in i:
        print(i)

#2.
print()

for i in range(100):
    if i%10==0:
        print(i)
#3.
print()

horton = "A person's a person, no matter how small."
vowels = 'aeiouAEIOU'

for letter in horton:
    if letter in vowels:
        print(letter)
