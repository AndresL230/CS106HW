#Andres Lopez
#CS 106 Section 009
#September 21, 2024

#1.
grades = ['A', 'F', 'C', 'F', 'A', 'B', 'A', 'C', 'A', 'B']
frequency = []

frequency.append(grades.count('A'))
frequency.append(grades.count('B'))
frequency.append(grades.count('C'))
frequency.append(grades.count('D'))
frequency.append(grades.count('F'))

print(frequency)

#2.

#a
print()
dog_breeds = []

dog_breeds.append('collie')
dog_breeds.append('sheepdog')
dog_breeds.append('Chow')
dog_breeds.append('Chihuahua')

print(dog_breeds)

#b
print()

herding_dogs = []

herding_dogs.append(dog_breeds[0])
herding_dogs.append(dog_breeds[1])

print(herding_dogs)

#c
print()

tiny_dogs = []

tiny_dogs.append(dog_breeds[3])

print(tiny_dogs)

#d
print()

print('Persian' in dog_breeds)
