#imports 
from Bio.Seq import Seq
from Bio import SeqIO
from Bio import Align
from Bio.SeqRecord import SeqRecord
from Bio.Align.Applications import ClustalwCommandline
from Bio import AlignIO
import custom_types


def extract_record_info(path, filename):
        segment_hemagglutinin = list(SeqIO.parse(path + filename, "fasta"))
        #For loop for turning the .fa files into a list of sequences that can be transformed  

        sequence_record_information = []

        for sequence in segment_hemagglutinin: 
                segment_hemagglutinin_text = sequence.seq.upper()
                segment_hemagglutinin_sequence = Seq(segment_hemagglutinin_text)
                # print(len(segment_hemagglutinin_sequence))
                forward_sequence = segment_hemagglutinin_sequence[0:200]
                reverse_sequence = segment_hemagglutinin_sequence[-200:]
                sr = custom_types.SequenceRecordInformation(forward_sequence, reverse_sequence, len(forward_sequence), len(reverse_sequence), sequence.id, sequence.description)
                sequence_record_information.append(sr)
        return sequence_record_information


def print_sequence_record_info(sequence_record_information):
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
def sequence_record_objects(sequence_record_information):
        forward_sequence_records = []
        reverse_sequence_records = []

        for record_information in sequence_record_information: 
                forward_record = SeqRecord(record_information.ForwardSequence, id = record_information.Id, description = record_information.Description)
                reverse_record = SeqRecord(record_information.ReverseSequence, id = record_information.Id, description= record_information.Description)
                forward_sequence_records.append(forward_record)
                reverse_sequence_records.append(reverse_record)
        return forward_sequence_records, reverse_sequence_records


# Write forward primers
def forward_primers(primer_sequence, id, description):
  forward_primer = SeqRecord(Seq(primer_sequence), id = id, description = description)
  SeqIO.write(forward_primer, "primer_fasta_files/" + id +"_primer.fasta", "fasta")

# Write reverse primers
def reverse_primers(primer_sequence, id, description): 
  reverse_primer = Seq(primer_sequence)
  reverse_compliment = Seq(reverse_primer.reverse_compliment())
  revcomp_primer = SeqRecord(Seq(reverse_compliment), id = id, description = description)
  SeqIO.write(revcomp_primer, "primer_fasta_files/" + id +"primer.fasta", "fasta")

# create primer tupple 
def create_primer_tupple(path, filename): 
        primer_sequence = list(SeqIO.parse(path + filename, "fasta"))[0]
        filename_list = filename.split("_")
        primer_info = custom_types.PrimerInformation(filename_list[0], filename_list[1], filename_list[2], filename_list[3] == "revcomp", primer_sequence.seq, primer_sequence.id, primer_sequence.description)
        return primer_info




def edited_sequences_fasta(records, filename):
        SeqIO.write(records, "edited_sequences/" + filename, "fasta")

###ClustalW alignment 
def clustalw_alignment(filename):
        cline = ClustalwCommandline("clustalw2", infile= "edited_sequences/" + filename + ".fasta")

        stdout, stderr = cline()

        align = AlignIO.read("alignments/" + filename + ".aln", "clustal")
        return align
        




