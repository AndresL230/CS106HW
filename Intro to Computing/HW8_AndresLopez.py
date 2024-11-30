#Andres Lopez
#CS 106 009
#HW 08, November 25, 2024

#Problem 1
def twoWords(length, firstLetter):
    lst = []
    while True:
        lengthWord = input('Enter a '+ str(length)+'-letter word: ')
        if length != len(lengthWord):
            lengthWord = input('Enter a '+ str(length)+'-letter word: ')
        else:
            lst.append(lengthWord)
            break
    while True:
        firstWord = input('Enter a word beginning with '+firstLetter+': ')
        if firstLetter != firstWord[0]:
            firstWord = input('Enter a word beginning with '+firstLetter+': ')
        else:
            lst.append(firstWord)
            break
    return lst
print(twoWords(5,'n'))

#Problem 2
def twoWordsV2(length, firstLetter):
    lengthWord = input('Enter a '+ str(length)+'-letter word: ')
    firstWord = input('Enter a word beginning with '+firstLetter+': ')    
    lst1 = []
    while length != len(lengthWord):
        lengthWord = input('Enter a '+ str(length)+'-letter word: ')
    lst1.append(lengthWord)
    while firstLetter != firstWord[0]:
        firstWord = input('Enter a word beginning with '+firstLetter+': ')
    lst1.append(firstWord)
    return lst1
print(twoWordsV2(10,'s'))

#Problem 3
def enterNewPassword():
    while True:
        password = input('Enter Password(8-15 characters and at least 1 digit): ')
        if len(password) >= 8 and len(password) <= 15:
            if password.isalpha() == True:
                password = input('Enter Password(8-15 characters and at least 1 digit): ')
            break
    return password
print(enterNewPassword())
    
#Problem 4
import random
number = random.randint(0,50)
def GuessNumber():
    for i in range(5):
        guess = int(input('Guess '+str(i+1)+': '))
        if guess == number:
            print('You are right I was thinking of '+ str(number)+'!')
            break
        elif guess<number:
            print('The number I was thinking of was higher')
        elif guess>number:
            print('The number I was thinking of is lower')
    print('I was actually thinking of '+str(number))
GuessNumber()
