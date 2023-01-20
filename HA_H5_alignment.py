#imports 
from collections import namedtuple

SequenceRecordInformation = namedtuple("SequenceRecordInformation", ["ForwardSequence", "ReverseSequence", "ForwardSequenceLength", "ReverseSequenceLength", "Id", "Description"])

from Bio.Seq import Seq
from Bio import SeqIO
from Bio import Align
from Bio.SeqRecord import SeqRecord
from Bio.Align.Applications import ClustalwCommandline
from Bio import AlignIO


#For loop for turning the .fa files into a list of sequences that can be transformed  
HA_H5 = list(SeqIO.parse("sequences/HA_H5_sequences.fa", "fasta"))

sequence_record_information = []

for sequence in HA_H5: 
        HA_H5_text = sequence.seq.upper()
        HA_H5_sequence = Seq(HA_H5_text)
        # print(len(HA_H5_sequence))
        forward_sequence = HA_H5_sequence[0:200]
        reverse_sequence = HA_H5_sequence[-200:]
        sr = SequenceRecordInformation(forward_sequence, reverse_sequence, len(forward_sequence), len(reverse_sequence), sequence.id, sequence.description)
        sequence_record_information.append(sr)



#For loop for extracting the sequence record information from the transformed sequences, and printing sequence record information for confirmation 
for sequences in sequence_record_information:
        print(f'Sequence ID: {sequences.Id}')
        print(f'Sequence Description: {sequences.Description}')
        print(f'Forward Sequence: {sequences.ForwardSequence}')
        print(f'Reverse Sequence: {sequences.ReverseSequence}')
        print(f'Forward Sequence Length: {sequences.ForwardSequenceLength}')
        print(f'Reverse Sequence Length: {sequences.ReverseSequenceLength}') 
        print()


#Turning edited sequences into sequence record object to be used in alignments 

forward_sequence_records = []
reverse_sequence_records = []

for record_information in sequence_record_information: 
    forward_record = SeqRecord(record_information.ForwardSequence, id = record_information.Id, description = record_information.Description)
    reverse_record = SeqRecord(record_information.ReverseSequence, id = record_information.Id, description= record_information.Description)
    forward_sequence_records.append(forward_record)
    reverse_sequence_records.append(reverse_record)


#Making the primers into sequence record objects, and saving them as .fasta files  
HA_forward_primer_1= SeqRecord(Seq("AGCAAAAGCAGGGGATAATTCTATTAAC"), id= "HA_Forward_1.6", description= "Forward primer 1")
HA_forward_primer_2= SeqRecord(Seq("CAAAAGCAGGGGGAAAACAAAAGAA"), id= "HA_Forward_1.7", description= "Forward primer 2")
HA_reverse_primer= Seq("CAAGGGTGTTTTTCTCATGATTCTGAA")
HA_reverse_compliment = Seq(HA_reverse_primer.reverse_complement())
HA_revcomp_primer= SeqRecord(Seq(HA_reverse_compliment), id= "HA_Reverse_2.3", description= "Reverse primer reverse compliment")

SeqIO.write(HA_forward_primer_1, "HA_forward_primer_1.fasta", "fasta")
SeqIO.write(HA_forward_primer_2, "HA_forward_primer_2.fasta", "fasta")
SeqIO.write(HA_revcomp_primer, "HA_revcomp_primer.fasta", "fasta")


#List of sequences to be aligned
HA_H5_edited_forward = forward_sequence_records + [HA_forward_primer_1, HA_forward_primer_2]
HA_H5_edited_reverse = reverse_sequence_records + [HA_revcomp_primer]


#Saving list of sequences to be aligned as .fasta files 
SeqIO.write(HA_H5_edited_forward, "HA_H5_edited_forward.fasta", "fasta")
SeqIO.write(HA_H5_edited_reverse, "HA_H5_edited_reverse.fasta", "fasta")


###ClustalW alignment 
#Forward sequences alignment
cline = ClustalwCommandline("clustalw2", infile='HA_H5_edited_forward.fasta')
print(cline)

stdout, stderr = cline()

align = AlignIO.read("HA_H5_edited_forward.aln", "clustal")
print(align)


#Reverse sequences alignment 
cline = ClustalwCommandline("clustalw2", infile='HA_H5_edited_reverse.fasta')
print(cline)

stdout, stderr = cline()

align = AlignIO.read("HA_H5_edited_reverse.aln", "clustal")
print(align)



