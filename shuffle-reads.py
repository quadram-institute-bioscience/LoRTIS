# This takes as input (concatenated) Illumina fastq reads
# python3 shuffle-reads.py FOSFOrep1-2MIC1mM_S32_L999_R1_001.fastq

from Bio import SeqIO

# Support gzipped reads..

import sys
import random

filename = sys.argv[1]
n_reads = int(sys.argv[2])

n=0

id2sequence=dict()
id2strand=dict()
id2quality=dict()


with open(filename) as f:
    lines = f.readlines()
    for line in lines:
        line_type = n%4
        if line_type==0: ident = line.rstrip()
        elif line_type==1:
            sequence = line.rstrip()
            id2sequence[ident] = sequence
        elif line_type==2:
            strand = line.rstrip()
            id2strand[ident] = strand
        elif line_type==3:
            quality = line.rstrip()
            id2quality[ident] = quality
        
        n=n+1

keylist = list(id2sequence.keys())

random.shuffle(keylist)
    

for i in range(0,n_reads):
    key = keylist[i]
    print(key)
    print(id2sequence[key])
    print(id2strand[key])
    print(id2quality[key])

