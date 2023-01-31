#imports 
from Bio.Seq import Seq
from Bio import SeqIO
from Bio import Align
from Bio.SeqRecord import SeqRecord
from Bio.Align.Applications import ClustalwCommandline
from Bio import AlignIO
import custom_types


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




# edited forward sequences to .fasta files 
def edited_forward_sequences_fasta(forward_sequence_records, *forward_primer_record, filename):
        edited_forward_record = forward_sequence_records + list(forward_primer_record)
        SeqIO.write(edited_forward_record, "edited_sequences/" + filename, "fasta")

#edited reverse sequences to .fasta files 
def edited_reverse_sequences_fasta(reverse_sequence_records, *revcomp_primer_record, filename):
        edited_reverse_record = reverse_sequence_records + list(revcomp_primer_record)
        SeqIO.write(edited_reverse_record, "edited_sequences/" + filename, "fasta")


###ClustalW alignment 
def clustalw_alignment(filename):
        cline = ClustalwCommandline("clustalw2", infile= "edited_sequences/" + filename + ".fasta")

        stdout, stderr = cline()

        align = AlignIO.read("alignments/" + filename + ".aln", "clustal")
        return align
        




