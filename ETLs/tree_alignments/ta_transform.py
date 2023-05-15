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
        sequences = segment_information[segment].EditedSequences
        for sequence in sequences:
                edited_sequences = sequence_record_objects(sequence)

                edited_tree_sequences = edited_sequences_fasta(segment, f"{segment}_{sequence[0].Strain}_edited_NCR.fasta", edited_sequences)
                

#Turning edited sequences into sequence record object to be used in alignments 
def sequence_record_objects(edited_sequence_record_information):
        sequence_records = []

        for record_information in edited_sequence_record_information: 
                sequence_record = SeqRecord(record_information.EditedSequence, id = record_information.Id, description = record_information.Description)
                sequence_records.append(sequence_record)
        return sequence_records

        
# edited forward sequences to .fasta files 
def edited_sequences_fasta(segment, filename, sequence_records):
        edited_record =sequence_records 
        SeqIO.write(edited_record, "db/" + segment + "/tree_sequences/" + filename, "fasta")


