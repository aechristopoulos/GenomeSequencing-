#imports 
from Bio.Seq import Seq
from Bio import SeqIO
from Bio import Align
from Bio.SeqRecord import SeqRecord
from Bio.Align.Applications import ClustalwCommandline
from Bio import AlignIO
import custom_types


def create_sequence_tupple(path, filename): 
        sequence_record = list(SeqIO.parse(path + filename, "fasta"))

        sequence_record_information = []

        for sequence in sequence_record: 
                sr = custom_types.SequenceRecordInformation(sequence, len(sequence), sequence.id, sequence.description)
                sequence_record_information.append(sr)
        return sequence_record_information




def create_edited_sequence_tupple(path, filename):
        segment_hemagglutinin = list(SeqIO.parse(path + filename, "fasta"))
        #For loop for turning the .fa files into a list of sequences that can be transformed  

        edited_sequence_record_information = []

        for sequence in segment_hemagglutinin: 
                segment_hemagglutinin_text = sequence.seq.upper()
                segment_hemagglutinin_sequence = Seq(segment_hemagglutinin_text)
                # print(len(segment_hemagglutinin_sequence))
                forward_sequence = segment_hemagglutinin_sequence[0:200]
                reverse_sequence = segment_hemagglutinin_sequence[-200:]
                esr = custom_types.EditedSequenceRecordInformation(forward_sequence, reverse_sequence, len(forward_sequence), len(reverse_sequence), sequence.id, sequence.description)
                edited_sequence_record_information.append(esr)
        return edited_sequence_record_information


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


#Turning edited sequences into sequence record object to be used in alignments 
def sequence_record_objects(edited_sequence_record_information):
        forward_sequence_records = []
        reverse_sequence_records = []

        for record_information in edited_sequence_record_information: 
                forward_record = SeqRecord(record_information.ForwardSequence, id = record_information.Id, description = record_information.Description)
                reverse_record = SeqRecord(record_information.ReverseSequence, id = record_information.Id, description= record_information.Description)
                forward_sequence_records.append(forward_record)
                reverse_sequence_records.append(reverse_record)
        return forward_sequence_records, reverse_sequence_records


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

# create primer tupple 
def create_primer_tupple(path, filename): 
        primer_sequence = list(SeqIO.parse(path + filename, "fasta"))[0]
        filename_list = filename.split("_")
        primer_info = custom_types.PrimerInformation(filename_list[0], filename_list[1], filename_list[2], filename_list[3] == "revcomp", primer_sequence.seq, primer_sequence.id, primer_sequence.description)
        return primer_info



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
        




