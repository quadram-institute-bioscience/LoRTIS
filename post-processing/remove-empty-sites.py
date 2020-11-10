# Remove the empty sites from an insertion plot

siteNumber=0
f = open('James2.out.gz.CP009273.insert_site_plot')
lines = f.readlines()
for line in lines:
    siteNumber+=1
    if not line=='0 0\n':
        field = line.rstrip().split(' ')
        if(int(field[0])>100000 or int(field[1])>100000):
            print(str(siteNumber) + " " + line)
