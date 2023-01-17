from Bio.Seq import Seq
from Bio import SeqIO
from Bio import Align
from Bio.SeqRecord import SeqRecord
from Bio.Align.Applications import ClustalwCommandline
from Bio import AlignIO


# #Making the primers into sequence record objects, and saving them as .fasta files  
# NS_forward_primer= SeqRecord(Seq("GCAAAAGCAGGGTGACAAA"), id= "NS Forward 1.2", description= "Forward primer")
# NS_reverse_primer= Seq("GATCAGTAGAAACAAGGGTGTT")
# NS_reverse_compliment = Seq(NS_reverse_primer.reverse_complement())
# NS_revcomp_primer= SeqRecord(Seq(NS_reverse_compliment), id= "NS Reverse 1.1", description= "Reverse primer reverse compliment")

# SeqIO.write(NS_forward_primer, "NS_forward_primer.fasta", "fasta")
# SeqIO.write(NS_revcomp_primer, "NS_revcomp_primer.fasta", "fasta")



#For loop for turning the .fa files into usable variables and returning the lengths of the sequences. 
NS_H9 = list(SeqIO.parse("sequences/NS_H9_sequences.fa", "fasta"))

for sequence in NS_H9: 
        NS_H9_text = sequence.seq.upper()
        NS_H9_sequence = Seq(NS_H9_text)
        print(len(NS_H9_sequence))
        forward_sequence = NS_H9_sequence[0:200]
        reverse_sequence = NS_H9_sequence[-200:]
        print(reverse_sequence)
        print(len(reverse_sequence))



#Editing sequences for the first and last 200 basepairs 
# victoria_forward = victoria_sequence[0:200]
# victoria_reverse = victoria_sequence[679:879]
# victoria_reverse_complement = victoria_reverse.reverse_complement()
# print("First 200 bp of Victoria H3N2 NS:", victoria_forward)
# print(len(victoria_forward)) 200
# print("Last 200 bp of Victoria H3N2 NS:", victoria_reverse)
# print(len(victoria_reverse)) 200
# print(victoria_reverse_compliment)







# #ClustalW alignment 
# cline = ClustalwCommandline("clustalw2", infile="sequences/NS_H9_sequences.fa")
# print(cline)

# stdout, stderr = cline()

# align = AlignIO.read("sequences/NS_H9_sequences.aln", "clustal")
# print(align)

