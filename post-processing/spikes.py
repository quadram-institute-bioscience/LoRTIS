# This script analyses a BioTradis plot file and determines the spikes
# A spike has a start, end (from which to infer width), maximum height, pattern, strand
# Any site with >=3 insertions should be part of this spike

threshold=5
siteNumber=1
maxHeight=0
spikeStart=1
pattern=''

outputfile = open('spikes.csv','w+')
outputfile.write('start,end,maxHeight,pattern,strand\n')

with open('biotin1308-trimmed.fasta.CP009273.1.insert_site_plot') as f:
    lines = f.readlines()
    for line in lines:
        fields = line.rstrip().split(' ')
        
        if int(fields[0])<threshold or siteNumber==len(lines):
            if maxHeight>0:
                outputfile.write(str(spikeStart) + ',' + str(siteNumber) + ',' + str(maxHeight) + ',' + pattern[:-1] + ',positive\n')
            
            spikeStart=siteNumber
            maxHeight=0
            pattern=''
        else:
            pattern+=fields[0] + ' '
            if int(fields[0])>maxHeight: maxHeight = int(fields[0])

        siteNumber=siteNumber+1

outputfile.flush()
outputfile.close()
