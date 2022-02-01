# Usage python3 reduce-insertion-plot.py barcode01tt.fa.CP009273.1.insert_site_plot 10000 to keep 10,000 insertions and make a new file with .reduced on the end

import sys
import random

filename = sys.argv[1]
numberOfInsertions = sys.argv[2]
lineNumber=0

insertions=list()

with open(filename) as f:
    lines=f.readlines()
    for line in lines:
        field = line.rstrip().split(' ')
        for forward in range(0,int(field[0])):
            insertions.append('f' + str(lineNumber))

        for reverse in range(0,int(field[1])):
            insertions.append('r' + str(lineNumber))

        lineNumber=lineNumber+1


random.shuffle(insertions)

newForwardInsertions = dict()
newReverseInsertions = dict()

for i in range(0,int(numberOfInsertions)):
    insertion = insertions[i]
    if insertion[0]=='f':
        position = int(insertion[1:])
        if not position in newForwardInsertions: newForwardInsertions[position]=1
        else: newForwardInsertions[position]=newForwardInsertions[position]+1

    if insertion[0]=='r':
        position = int(insertion[1:])
        if not position in newReverseInsertions: newReverseInsertions[position]=1
        else: newReverseInsertions[position]=newReverseInsertions[position]+1



for i in range(0,lineNumber):
    line=''
    if i in newForwardInsertions: line = str(newForwardInsertions[i])
    else: line = '0'

    line = line + ' '

    if i in newReverseInsertions: line = line + str(newReverseInsertions[i])
    else: line = line + '0'

    print(line)
