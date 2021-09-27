#code to find course codes in text files by Connor McMillan

#import regex tools
import re

#----- Open file and create list of strings -----#
#open file in read only
file = open('FakeAssign.txt', 'r')
f = file.readlines()

#creates a string of each line and converts each line into a list indent
newlist = []
for line in f:
    if line[-1] == '\n':
        newlist.append(line[:-1])

#----- Regex to find unit code(s) -----#
#creates a pattern for x amount of characters that end before "COS"
pattern = re.compile('.*[a-zA-Z]{3}[0-9]{5}')
for i in newlist:
    match_string = i
    result = re.match(pattern, match_string)
    if result:
        #print("search successful")
        print(match_string)
        print(result)