#Andres Lopez
#CS 106 009
#HW 06, October 21, 2024

#1.
#a.
def hasFinalLetter(strList,letters):
    lttrList = []
    for i in strList:
        if i[-1] in letters:
            lttrList.append(i)
    return lttrList

#b.
random_words1 = ["Quasar", "Luminous", "Jumble", "Serendipity", "Zephyr"]
print(hasFinalLetter(random_words1,'res'))

random_words2 = ["Eclipse", "Whimsical", "Labyrinth", "Crescent", "Voyage"]
print(hasFinalLetter(random_words2,'res'))

random_words3 = ["Tranquil", "Mosaic", "Echo", "Nebula", "Horizon"]
print(hasFinalLetter(random_words3,'res'))

#2.
print()
#a.
def isDivisible(maxInt, twoInts):
    divisible = []
    for i in range(1,maxInt):
        if i%twoInts[0] == 0 and i%twoInts[1] == 0:
            divisible.append(i)
    return divisible

#b.
print(isDivisible(28,(2,3)))

print(isDivisible(70,(3,5)))

print(isDivisible(20,(7,3)))
