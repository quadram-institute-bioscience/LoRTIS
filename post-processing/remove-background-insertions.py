import sys

filename = sys.argv[1]
threshold = 0

if len(sys.argv)>2: threshold = int(sys.argv[2])

with open(filename) as f:
    lines = f.readlines()
    for line in lines:
        fields = line.rstrip().split(' ')

        positivereads = int(fields[0])
        if positivereads<threshold: positivereads=0

        negativereads = int(fields[1])
        if abs(negativereads)<threshold: negativereads=0
#        else: negativereads = -negativereads
        
        print(str(positivereads) + ' ' + str(negativereads))

    f.close()
