# This takes as input a .sam file
# Don't use samtools to keep best map
# sam tools to keep best read only?
# Is this going to use a shed load of memory?


# Usage python3 keep-uniquely-mapping-reads-only.py biotin1308-trimmed.nonunique.sam
# samtools view -S -b biotin1308-trimmed.unique.sam > biotin1308-trimmed.unique.bam
# samtools sort biotin1308-trimmed.unique.bam -o biotin1308-trimmed.unique.sorted.bam

import sys

filename = sys.argv[1]

id2freq = dict()
id2line=dict()

outputfile = open(filename + '.unique','w+')

with open(filename) as f:
    lines = f.readlines()
    for line in lines:
        if line[0]=='@':
            outputfile.write(line)
        else:
            fields = line.split('\t')
            ident = fields[0]
            if ident not in id2freq.keys():
                id2freq[ident]=1
                id2line[ident]=line
            else: id2freq[ident] = id2freq[ident] + 1

for ident in id2freq.keys():
    if id2freq[ident]==1:
        outputfile.write(id2line[ident])

outputfile.flush()
outputfile.close()
