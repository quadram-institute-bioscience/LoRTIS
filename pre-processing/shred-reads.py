from Bio import SeqIO

#from StringIO import StringIO
import io

import subprocess
import sys
from subprocess import Popen, PIPE, STDOUT
from io import StringIO

filename = sys.argv[1]
shred_length=75

with open(filename + '.shreaded',"w+") as f:
    for record in SeqIO.parse(filename, "fasta"):
        ident = record.id
        sequence = record.seq

        for i in range(0,len(sequence)//shred_length):
            startIndex = i*shred_length
            endIndex = (i+1)*shred_length
            
            f.write('>' + ident + '_' + str(i) + '\n')
            f.write(str(sequence[startIndex:endIndex])  + '\n')


        startIndex = (len(sequence)//shred_length)*shred_length
        finalsubsequence = str(sequence[startIndex:])
        
        if len(finalsubsequence) > 0:
            f.write('>' + ident + '_final\n')
            f.write(finalsubsequence  + '\n')
    
