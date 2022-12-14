from Bio.Align.Applications import MuscleCommandline
from io import StringIO
from Bio import AlignIO


# cline = MuscleCommandline(input="sequences/NS_H9_sequences.fa", out="sequences/NS_H9_sequences.txt")
# print(cline)


# muscle_cline = MuscleCommandline(input="NS_H9_sequences.fa", out= "aln.afa")
# stdout, stderr = muscle_cline()
# align = AlignIO.read(StringIO(stdout), "fasta")
# # print(align)


# import subprocess
# result = subprocess.run(['dir'], stdout=subprocess.PIPE, shell = True)
# print(result.stdout)

# import subprocess
# result = subprocess.run(['echo', 'hello'], stdout=subprocess.PIPE, shell=True)
# print(result.stdout)

## Run muscle -align 
import subprocess
result = subprocess.run(['muscle', '-align', 'sequences/NS_H9_sequences.fa', '-output', 'aln.afa'], stdout=subprocess.PIPE, shell = True)
print(result.stdout)

##Open outputfile (-aln.afa)
