from Bio.Align.Applications import MuscleCommandline
from io import StringIO
from Bio import AlignIO


# cline = MuscleCommandline(input="sequences/NS_H9_sequences.fa", out="sequences/NS_H9_sequences.txt")
# print(cline)


muscle_cline = MuscleCommandline(input="sequences/NS_H9_sequences.fa")
stdout, stderr = muscle_cline()
align = AlignIO.read(StringIO(stdout), "fasta")
print(align)