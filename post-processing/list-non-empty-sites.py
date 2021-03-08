import sys

max1=0
max2=0
insertions=0

filename = sys.argv[1]

lineNumber=0
with open(filename) as f:
    lines = f.readlines()
    for line in lines:
        lineNumber=lineNumber+1
        if not line=='0 0\n':
            fields = line.split(' ')
            if int(fields[0])>max1 : max1=int(fields[0])
            if int(fields[1])>max2 : max2=int(fields[1])
            
            insertions=insertions+int(fields[0])
            insertions=insertions+int(fields[1])
            
            print(str(lineNumber) + "," + line.rstrip());

print(max1)
print(max2)
print(insertions)
