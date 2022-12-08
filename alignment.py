from Bio import pairwise2 #does pairwise alignments 
from Bio.pairwise2 import format_alignment #formats pairwise alignments to be more readable
from Bio.Seq import Seq 
from Bio import Align
from Bio.Align.Applications import ClustalwCommandline
from Bio import SeqIO

# with open("sequences/A_Victoria_361_2011_H3N2_NS.fasta", "r") as f:
#   victoria_text = f.read()

# with open("sequences/A_Brisbane_59_2007_H1N1_NS.fasta", "r") as t:
#   brisbane_text = t.read()

# seq1 = Seq(victoria_text)
# seq2 = Seq(brisbane_text)

victoria_text = list(SeqIO.parse("sequences/A_Victoria_361_2011_H3N2_NS.fasta", "fasta"))[0].seq.lower()
brisbane_text = list(SeqIO.parse("sequences/A_Brisbane_59_2007_H1N1_NS.fasta", "fasta"))[0].seq.lower()

print(victoria_text)
print(brisbane_text)

victoria_sequence = Seq(victoria_text)
brisbane_sequence = Seq(brisbane_text)

alignments = pairwise2.align.globalxx(victoria_sequence, brisbane_sequence)

# for alignment in alignments: 
#      print(alignment)


# alignments = pairwise2.align.globalxx(seq1, seq2) 
# for alignment in alignments: 
#         print(format_alignment(*alignment)) 


victoria_sequence = Seq(victoria_text)
brisbane_sequence = Seq(brisbane_text)

alignments = Align.PairwiseAligner().align(victoria_sequence, brisbane_sequence)

# for alignment in alignments: 
#     print(alignment)


###ClustalW alignment 
cline = ClustalwCommandline("clustalw2", infile="NS_H1_sequences.fa")
# print(cline)

from Bio import AlignIO
align = AlignIO.read(victoria_sequence, brisbane_sequence, "clustal")
print(align)