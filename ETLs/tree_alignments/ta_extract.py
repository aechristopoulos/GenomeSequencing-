# imports
from Bio import SeqIO
import os
import ta_custom_types
from Bio.Seq import Seq

# Extract Function 
def extract(absolute_path):
    segment_information = {}
    path = absolute_path + "/db/"
    db = os.scandir(path)
    for entry in db: 
        if entry.is_dir():
            sequence_info = parse_sequences(path, entry.name)
            edited_sequence_info = parse_edited_sequences(path, entry.name)
            segment_information[entry.name] = ta_custom_types.DirectoryInformation(Sequences=sequence_info, EditedSequences=edited_sequence_info)
    return segment_information 


# create sequence tupple function 
def create_sequence_tupple(path, filename): 
        filename_list = filename.split("_")
        sequence_record = list(SeqIO.parse(path + filename, "fasta"))

        sequence_record_information = []

        for sequence in sequence_record: 
                sr = ta_custom_types.SequenceRecordInformation(filename_list[0], filename_list[1], sequence, len(sequence), sequence.id, sequence.description)
                sequence_record_information.append(sr)
        return sequence_record_information

# create edited sequences tupple function, returns a list of edited sequences 
def create_edited_sequence_tupple(path, filename):
        filename_list=filename.split("_")
        segment_hemagglutinin = list(SeqIO.parse(path + filename, "fasta"))

        #For loop for turning the .fa files into a list of sequences that can be transformed  
        edited_sequence_record_information = []

        for sequence in segment_hemagglutinin: 
                segment_hemagglutinin_text = sequence.seq.upper()
                segment_hemagglutinin_sequence = Seq(segment_hemagglutinin_text)
                edited_sequence = segment_hemagglutinin_sequence
                esr = ta_custom_types.EditedSequenceRecordInformation(filename_list[0], filename_list[1], edited_sequence, len(sequence), sequence.id, sequence.description)
                edited_sequence_record_information.append(esr)
        return edited_sequence_record_information

# creates sequences dictionary 
def parse_sequences(path, sequence):
    sequence_path = path + sequence + "/sequences/"
    sequence_folder = os.scandir(sequence_path)
    sequences = []
    for entry in sequence_folder:
        if entry.is_file():
            sequence_tupple = create_sequence_tupple(sequence_path, entry.name)
            sequences.append(sequence_tupple)
    return sequences


# creates edited sequences dictionary 
def parse_edited_sequences(path, edited_sequence):
    edited_sequence_path = path + edited_sequence + "/sequences/"
    edited_sequence_folder = os.scandir(edited_sequence_path)
    edited_sequenes = []
    for entry in edited_sequence_folder:
        if entry.is_file():
            edited_sequence_tupple = create_edited_sequence_tupple(edited_sequence_path, entry.name)
            edited_sequenes.append(edited_sequence_tupple)
    return edited_sequenes
