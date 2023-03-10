#imports
from Bio import SeqIO
from Bio.SeqRecord import SeqRecord
import os 

# transform function 
def transform(absolute_path, segment_information):
        path = absolute_path + "/db/"
        db = os.scandir(path)
        for entry in db: 
                if entry.is_dir():
                        do_transform(segment_information, entry.name)

# Gets information needed to do transform function 
def do_transform(segment_information, segment):
        primers = segment_information[segment].Primers
        sequences = segment_information[segment].EditedSequences
        forward_primers, reverse_primers = primer_record_objects(primers)
        for sequence in sequences:
                forward_edited_sequences, reverse_edited_sequences =sequence_record_objects(sequence)

                forward_sequences = edited_forward_sequences_fasta(segment, f"{segment}_{sequence[0].Strain}_edited_forward_NCR.fasta", forward_edited_sequences, forward_primers)
                reverse_sequences = edited_reverse_sequences_fasta(segment, f"{segment}_{sequence[0].Strain}_edited_reverse_NCR.fasta", reverse_edited_sequences, reverse_primers)
   

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

# Turns primer .fasta files into record objects that can be used in other functions 
def primer_record_objects(primer_information):
        forward_primer_records = []
        reverse_primer_records = []

        for primer in primer_information:
                if primer.Direction == "Forward":
                        forward_primer = SeqRecord(primer.Sequence, id= primer.Id, description= primer.Description)
                        forward_primer_records.append(forward_primer)
                if primer.Direction == "Reverse": 
                        reverse_primer = SeqRecord(primer.Sequence, id = primer.Id, description= primer.Description)
                        reverse_primer_records.append(reverse_primer)
        return forward_primer_records, reverse_primer_records
        
# edited forward sequences to .fasta files 
def edited_forward_sequences_fasta(segment, filename, forward_sequence_records, forward_primers):
        edited_forward_record = forward_sequence_records + forward_primers
        SeqIO.write(edited_forward_record, "db/" + segment + "/edited_sequences/" + filename, "fasta")

#edited reverse sequences to .fasta files 
def edited_reverse_sequences_fasta(segment, filename, reverse_sequence_records, reverse_primers):
        edited_reverse_record = reverse_sequence_records + reverse_primers
        SeqIO.write(edited_reverse_record, "db/" + segment + "/edited_sequences/" + filename, "fasta")
