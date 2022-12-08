from Bio import pairwise2 #does pairwise alignments 
from Bio.pairwise2 import format_alignment #formats pairwise alignments to be more readable
from Bio.Seq import Seq 


seq1 = Seq(open("A_Victoria_361_2011_H3N2_NS.fasta", "r"))
seq2 = Seq(open("A_Brisbane_59_2007_H1N1_NS.fasta", "r"))

alignments = pairwise2.align.globalxx(seq1, seq2)

# for alignment in alignments: 
#     print(alignment)


alignments = pairwise2.align.globalxx(seq1, seq2) 
for alignment in alignments: 
        print(format_alignment(*alignment)) 
