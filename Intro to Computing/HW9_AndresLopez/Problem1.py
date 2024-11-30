#Andres Lopez
#CS 106 009
#HW 09, November 27, 2024
import string
#Problem 1
def file_copy(in_file, out_file):
    source = open(in_file, 'r')
    content = source.readlines()
    source.close()
    copyf = open(out_file, 'w')
    for line in content:
        copyf.write(line)
    copyf.close()
file_copy('created_equal.txt', 'Copy1.txt')

#Problem 2
def file_stats(in_file):
    statfile = open(in_file, 'r')
    filelst = statfile.readlines()
    wrdlst = []
    for string in filelst:
        wrdlst += string.split(' ')
    counter = 0
    for string in filelst:
        counter+=len(string)
    return ('Lines: '+str(len(filelst))+'\nWords: '+str(len(wrdlst))+'\nCharacters: '+str(counter))

print(file_stats('created_equal.txt'))

#Problem 3
def repeat_words(in_file, out_file):
    file_one = open(in_file, 'r')
    content = file_one.readlines()
    file_one.close()
    fstlst = []
    for text in content:
        fstlst += text.split()
    scndlst = []
    for wrd in fstlst:
        scndlst.append(wrd.lower())
    thrdlst = []
    for text in scndlst:
        thrdlst.append(text.strip(string.punctuation))
    #for x in thrdlst:
    #    thrdlst.remove(x)
        
    return thrdlst
    #strpfile = open(out_file, 'w') text.strip(string.punctuation)

print(repeat_words('CatintheHat.txt', 'catRepWords.txt'))
