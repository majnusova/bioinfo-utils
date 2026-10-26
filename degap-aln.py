""" 
Removes gaps from FASTA alignments without introducing unwanted whitespace or newline characters.

USAGE: python3 degap-aln.py input_filenaname output_filename
"""

import sys
from Bio import SeqIO

input_file = sys.argv[1]
output_file = sys.argv[2]

def degap_aln(input_file, output_file):
    with open(output_file, "w") as outf:
        for record in SeqIO.parse(input_file, "fasta"):
            record.seq = record.seq.replace("-","")
            SeqIO.write(record, outf, "fasta")

degap_aln(input_file, output_file)