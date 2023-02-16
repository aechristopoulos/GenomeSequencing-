#imports 
from Bio.Seq import Seq
from Bio import SeqIO
from Bio import Align
from Bio.SeqRecord import SeqRecord
from Bio.Align.Applications import ClustalwCommandline
from Bio.Align.Applications import ClustalOmegaCommandline
from Bio import AlignIO
import subprocess
import os

# Write forward primers
def forward_primers(primer_sequence, id, description):
  forward_primer = SeqRecord(Seq(primer_sequence), id = id, description = description)
  forward_primer_record = SeqIO.write(forward_primer, "primer_fasta_files/" + id +"_primer.fasta", "fasta")
  return forward_primer_record

# Write reverse primers
def reverse_primers(primer_sequence, id, description): 
  reverse_primer = Seq(primer_sequence)
  reverse_compliment = Seq(reverse_primer.reverse_compliment())
  revcomp_primer = SeqRecord(Seq(reverse_compliment), id = id, description = description)
  revcomp_primer_record = SeqIO.write(revcomp_primer, "primer_fasta_files/" + id +"primer.fasta", "fasta")
  return revcomp_primer_record



###ClustalW alignment 
def clustalw_alignment(segment, filename):
        cline = ClustalwCommandline("clustalw2", infile= "db/" + segment + "/edited_sequences/" + filename + ".fasta")

        stdout, stderr = cline()

        align = AlignIO.read("/alignments/" + filename + ".aln", "clustal")
        return align


def print_sequence_record_info(edited_sequence_record_information):
#For loop for extracting the sequence record information from the transformed sequences, and printing sequence record information for confirmation 
        for sequences in edited_sequence_record_information:
                print(f'Sequence ID: {sequences.Id}')
                print(f'Sequence Description: {sequences.Description}')
                print(f'Forward Sequence: {sequences.ForwardSequence}')
                print(f'Reverse Sequence: {sequences.ReverseSequence}')
                print(f'Forward Sequence Length: {sequences.ForwardSequenceLength}')
                print(f'Reverse Sequence Length: {sequences.ReverseSequenceLength}') 
                print()
