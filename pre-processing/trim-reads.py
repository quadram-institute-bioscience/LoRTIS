# This trims the reads based on the position and orientation of the Minimap2 results, split into positive and negative reads
from Bio.Align.Applications import MuscleCommandline
from Bio import SeqIO

#from StringIO import StringIO
import io

import subprocess
import sys
from subprocess import Popen, PIPE, STDOUT
from io import StringIO
import sys


def outputTrimmedRead(ident,read,trimmedReads):
    p = Popen(['/usr/bin/muscle'], stdout=PIPE, stdin=PIPE, stderr=STDOUT)
    unaligned = '>' + ident + '\n' + read + '\n>transposon\nGATAACAATTTCACACAGGAAACAGCCAGTCCGTTTAGGTGTTTTCACGAGCACTGCAGGCATGCCAGGGTTGAGATGTGTATAAGAGACAG\n>transposon_rc\nCTGTCTCTTATACACATCTCAACCCTGGCATGCCTGCAGTGCTCGTGAAAACACCTAAACGGACTGGCTGTTTCCTGTGTGAAATTGTTATC\n'
    muscle_stdout = p.communicate(input=str.encode(unaligned))[0]

    output = muscle_stdout.decode()
    if '>' in output:
        output = output[output.index('>'):]

        # Lets evaluate the score for the transposon and the reverse compliement
        name2seq = dict()

        readid=''

        # Load the alignment
        for record in SeqIO.parse(StringIO(output), "fasta"):
            ident = record.id
            if not ident[0]=='t':
                readid=ident
            sequence = record.seq
            name2seq[ident] = sequence


        read = name2seq[readid]
        transposon = name2seq['transposon']
        transposon_rc = name2seq['transposon_rc']

        transposon_score=0
        transposon_rc_score=0

        for i in range(0,len(read)):
            if transposon[i]==read[i]:transposon_score+=1
            if transposon_rc[i]==read[i]:transposon_rc_score+=1

     #   print('transposon_score: ' + str(transposon_score))
     #   print('transposon_rc_score: ' + str(transposon_rc_score))

        if transposon_score>transposon_rc_score:
            transposon_str = str(transposon)
     #       print('matches transposon')

            gIndex = transposon_str.rfind('G')
            cIndex = transposon_str.rfind('C')
            aIndex = transposon_str.rfind('A')
            tIndex = transposon_str.rfind('T')

            endOfSequence=max(max(gIndex,cIndex),max(aIndex,tIndex))
            trimmedSequence = read[:endOfSequence]

            
            seq = str(trimmedSequence).replace('-','')
            if len(seq)>0:
                trimmedReads.write('>' + readid + '\n')
                trimmedReads.write(seq + '\n');
        else:
            transposon_rc_str = str(transposon_rc)
     #       print('matches rc')
            gIndex = transposon_rc_str.index('G')
            cIndex = transposon_rc_str.index('C')
            aIndex = transposon_rc_str.index('A')
            tIndex = transposon_rc_str.index('T')

            startOfSequence = min(min(gIndex,cIndex),min(aIndex,tIndex))
            trimmedSequence = read[:startOfSequence]

            seq = str(trimmedSequence.reverse_complement()).replace('-','')
            if len(seq)>0:
                trimmedReads.write('>' + readid + '\n')
                trimmedReads.write(seq + '\n');



filename = sys.argv[1]
trimmedReads = open(filename[:-6] + "t.fa", "w")

for record in SeqIO.parse(filename, "fastq"):
    ident = record.id
    sequence = record.seq
    outputTrimmedRead(str(ident),str(sequence),trimmedReads)

trimmedReads.flush()
trimmedReads.close()
