import sys
import gzip

from mimetypes import guess_type
from functools import partial
from Bio import SeqIO

input_file = sys.argv[1]
length = sys.argv[2]
taglength = int(length)

encoding = guess_type(input_file)[1]  # uses file extension
_open = partial(gzip.open, mode='rt') if encoding == 'gzip' else open

with _open(input_file) as f:
    for record in SeqIO.parse(f, 'fastq'):
        sequence = str(record.seq)
        
        if len(sequence)> taglength:
            print('>' + str(record.id))
            print(sequence[taglength:])
