# This takes as input (concatenated) Illumina fastq reads
# python3 shuffle-reads.py FOSFOrep1-2MIC1mM_S32_L999_R1_001.fastq 10000 > FOSFOrep1-2MIC1mM_S32_L999_R1_001.10000.fastq

from Bio import SeqIO

# Support gzipped reads..

import sys
import random

filename = sys.argv[1]

line_number=1
for line in open(filename):
    line_number=line_number+1

sequence_numbers=list()
for i in range(0,int(line_number/4)):
    sequence_numbers.append(i)

random.shuffle(sequence_numbers)

if len(sys.argv)>2: n_reads = int(sys.argv[2])
else: n_reads = int(line_number/4)

sequence_numbers_to_pick=set()
for i in range(0,n_reads):
    sequence_numbers_to_pick.add(sequence_numbers[i])


sequence_number=-1 # This will mean the first read is number zero as we add 1 when we read the first line

n=0
for line in open(filename):
    line_type = n%4
    if line_type==0: sequence_number=sequence_number+1
    if sequence_number in sequence_numbers_to_pick: print(line.rstrip())
    n=n+1
