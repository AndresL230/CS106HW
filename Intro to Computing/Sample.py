#Andres Lopez
#CS 106 Section 009

'''
name = input('Enter your name: ')
age = int(input('Enter you age: '))
print(name + ', you will be ' + str(age + 1) + ' next year!')

name = input('Enter your name: ')
car_insurance = 100
year = int(input('Years with car insurance: '))
print(name+', your car insurance will be $'+str((year+1)*100)+' after '+str(year)+' years.')

age = 65
if age > 62:
    print('You can get Social Security benefits')

report = 'Yay! We are getting large bonuses this year'
if 'large bonuses' in(report):
    print('Vacation time!')

hits = 12
shield = 0
if hits > 10 and shield == 0:
    print("You're dead...")

age = 18

if age > 17:
    print('You can vote')
else:
    print("You can't vote")
print('Goodbye')

User_Name = input('Enter your Name: ')
User_Age = int(input('Enter your Age: '))


if User_Age > 70:
    Music = ('Beatles')
elif User_Age > 60:
    Music = ('Jazz')
elif User_Age > 40:
    Music = ('Disco')
else:
    Music = ('Coldplay')

print(User_Name + ', you like ' + Music + '!')


for i in range (0,11):
    print(i)

print()
for i in range (0,10):
    print(i)

print()
for i in range(0,9,2):
    print(i)

print()
for i in range(1,10,2):
    print(i)

print()
for i in range(20,70,10):
    print(i)

summation=0
user_sum = input('Until what number: ')
for i in range (int(user_sum)):
    summation=summation+i
print(summation)

user_product = input('What number: ')
for i in range(1, 13):
    print(int(user_product)*i)



def iSquaredPlus10(x):
    result = x**2+10
    return result

print(iSquaredPlus10(4))

def sumof(x,y):
    result=x+y
    return result

print(sumof(5,6))

def productof(x,y,z):
    result=x*y*z
    return result

print(productof(2,3,4))

def hello(name):
    print('Welcome, ' + name + ', to the world of Python.')


hello('Andres')

for - in range(5):
    print(-)

user_number = int(input('Input a number:'))

while user_number>0:
    user_number = int(input('Input a number:'))

print(user_number)

inFile = open("textsample.txt", "r")
print(inFile.read())
inFile.close()

hdList = ['Humpty Dumpty sat on a wall.', 'Humpty Dumpty had a great fall.',
          "All the king's horses and all the king's men", "Couldn't put Humpty together again!"]

outFile = open("humpty.txt", "w")
for line in hdList:
    outFile.write(line + '\n')
outFile.close()

inFile = open("humpty.txt", "r")
print(inFile.read())

humptyFile = open('humpty.txt', 'r')
for line in humptyFile:
    if 'Humpty' in line:
        print(line, end = '')

infile = open('example.txt')
print(infile.read(1))

students = {583721:['Alice','123 Elm St','Freshman',18,'Reading'],941237:['Bob','456 Oak St','Sophomore',19,'Cycling'],
            357469:['Charlie','789 Pine St','Freshman',19,'Swimming'],692840:['David','101 Maple St','Senior',21,'Gaming'],
            840216:['Eva','202 Birch St','Junior',20,'Photography'],273581:['Frank','202 Birch St','Sophomore',19,'Baking'],
            459732:['Grace','456 Cedar Ln','Freshman',19,'Painting'],105634:['Helen','590 Foxhill Dr','Senior',22,'Guitar'],
            728906:['Ivy','200 Silverwood Ave','Junior',20,'Chess'],315248:['Jack','654 Sunset Blvs','Junior',21,'Tennis']}

grades = [95, 96, 100, 85, 95, 90, 95, 100, 100]
def frequency(itemList):
    counters = {}
    for item in itemList:
        if item not in counters:
            counters[item] = 1
        else:
            counters[item] += 1
    return counters
print(frequency(grades))

#1
sample_dict = {'a':100, 'b':200, 'c':300}
for i in sample_dict.values():
    if i == 200:
        print(i)
#2
lst = [3,1,3,1,5,9,2,6,5,3,5]
dict1 = {}
for i in lst:
    if i not in dict1:
        dict1[i]= lst.index(i)
print(dict1)
'''
