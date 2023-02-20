from Bio.Seq import Seq
from Bio import SeqIO
from Bio import Align
from Bio.SeqRecord import SeqRecord
from Bio.Align.Applications import ClustalwCommandline
from Bio import AlignIO


#turning fasta files into usable variables
victoria_text = list(SeqIO.parse("sequences/A_Victoria_361_2011_H3N2_NS.fasta", "fasta"))[0].seq.upper()
brisbane_text = list(SeqIO.parse("sequences/A_Brisbane_59_2007_H1N1_NS.fasta", "fasta"))[0].seq.upper()

#turning the variables into sequence objects 
victoria_sequence = Seq(victoria_text)
brisbane_sequence = Seq(brisbane_text)

#Length of sequences 
# print(len(victoria_sequence)) 879
# print(len(brisbane_sequence)) 870 

#Editing sequences for the first and last 200 basepairs 
victoria_forward = victoria_sequence[0:200]
victoria_reverse = victoria_sequence[679:879]
victoria_reverse_complement = victoria_reverse.reverse_complement()
# print("First 200 bp of Victoria H3N2 NS:", victoria_forward)
# print(len(victoria_forward)) 
# print("Last 200 bp of Victoria H3N2 NS:", victoria_reverse)
# print(len(victoria_reverse)) 200
# print(victoria_reverse_compliment)

brisbane_foward = brisbane_sequence[0:200]
brisbane_reverse = brisbane_sequence [670:870]
bribane_reverses_complement = brisbane_sequence.reverse_complement()
# print(len(brisbane_foward)) 200
# print(len(brisbane_reverse)) 200

#Turning edited sequences into usable sequence record objects 
short_v_forward = SeqRecord(Seq(victoria_forward), id= "A|Victoria|361|2011|A\ H3N2|seasonal|NS|8|KJ942684.1", 
description="A/Victoria/361/2011(H3N2) segment 8 nonstructural protein (NS) first 200 bps")

short_v_reverse = SeqRecord(Seq(victoria_reverse), id = "A|Victoria|361|2011|A\ H3N2|seasonal|NS|8|KJ942684.1", 
description="A/Victoria/361/2011(H3N2) segment 8 nonstructural protein (NS) last 200 bps")

short_b_forward = SeqRecord(Seq(brisbane_foward), id ="A|Brisbane|59|2007|A\ H1N1|seasonal|NS|8|WSS3272077",
description= "A/Brisbane/59/2007(H1N1) segment 8 nonstructural protein (NS) first 200 bps")

short_b_reverse = SeqRecord(Seq(brisbane_reverse), id = "A|Brisbane|59|2007|A\ H1N1|seasonal|NS|8|WSS3272077",
description= "A/Brisbane/59/2007(H1N1) segment 8 nonstructural protein (NS) last 200 bps")

#Making the primers into sequence record objects, and saving them as .fasta files  
NS_forward_primer= SeqRecord(Seq("GCAAAAGCAGGGTGACAAA"), id= "NS Forward 1.2", description= "Forward primer")
NS_reverse_primer= Seq("GATCAGTAGAAACAAGGGTGTT")
NS_reverse_compliment = Seq(NS_reverse_primer.reverse_complement())
NS_revcomp_primer= SeqRecord(Seq(NS_reverse_compliment), id= "NS Reverse 1.1", description= "Reverse primer reverse compliment")

SeqIO.write(NS_forward_primer, "NS_forward_primer.fasta", "fasta")
SeqIO.write(NS_revcomp_primer, "NS_revcomp_primer.fasta", "fasta")

#List of alignment objects
shortened_forward_example = [short_v_forward, short_b_forward, NS_forward_primer]
shortened_reverse_example = [short_v_reverse, short_b_reverse, NS_revcomp_primer]


#Saving alignment objects as .fasta files 
SeqIO.write(shortened_forward_example, "shortened_forward_example.fasta", "fasta")
SeqIO.write(shortened_reverse_example, "shortened_reverse_example.fasta", "fasta")



###ClustalW alignment 
#Forward sequences alignment
cline = ClustalwCommandline("clustalw2", infile='shortened_forward_example.fasta')
print(cline)

stdout, stderr = cline()

align = AlignIO.read("shortened_forward_example.aln", "clustal")
print(align)


#Reverse sequences alignment 
cline = ClustalwCommandline("clustalw2", infile='shortened_reverse_example.fasta')
print(cline)

stdout, stderr = cline()

align = AlignIO.read("shortened_reverse_example.aln", "clustal")
print(align)


