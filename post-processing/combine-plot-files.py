# Combine two plot files

import sys

filename1 = sys.argv[1]
filename2 = sys.argv[2]

mode='sum'
if len(sys.argv) > 3: mode = sys.argv[3]

plot1 = open(filename1)
lines1=plot1.readlines()

plot2 = open(filename2)
lines2=plot2.readlines()

if len(lines1)==len(lines2):
    for i in range(0,len(lines1)):
        field1 = lines1[i].rstrip().split(' ')
        field2 = lines2[i].rstrip().split(' ')

        if mode=='sum':
            positive = int(field1[0]) + int(field2[0])
            negative = int(field1[1]) + int(field2[1])
        elif mode=='min':
            positive = min(int(field1[0]),int(field2[0]))
            negative = min(int(field1[1]),int(field2[1]))
            
        print(str(positive) + ' ' + str(negative))
else:
    print('Error plot files are a different length, plot 1 is ' + str(len(lines1)) + ' whilst plot 2 is ' + str(len(lines2)))
