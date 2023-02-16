from Bio import SeqIO
import os  
import load
import os
import custom_types
from Bio.Seq import Seq

def extract():
    segment_information = {}
    path = "./db/"
    db = os.scandir(path)
    for entry in db: 
        if entry.is_dir():
            primer_info = parse_primers(path, entry.name)
            sequence_info = parse_sequences(path, entry.name)
            edited_sequence_info = parse_edited_sequences(path, entry.name)
            segment_information[entry.name] = custom_types.DirectoryInformation(EditedSequences=edited_sequence_info, Primers=primer_info, Sequences=sequence_info)
    return segment_information 

# create primer tupple 
def create_primer_tupple(path, filename): 
        primer_sequence = list(SeqIO.parse(path + filename, "fasta"))[0]
        filename_list = filename.split("_")
        primer_info = custom_types.PrimerInformation(filename_list[0], filename_list[1], filename_list[2], filename_list[3] == "revcomp", primer_sequence.seq, primer_sequence.id, primer_sequence.description)
        return primer_info


def create_sequence_tupple(path, filename): 
        filename_list = filename.split("_")
        sequence_record = list(SeqIO.parse(path + filename, "fasta"))

        sequence_record_information = []

        for sequence in sequence_record: 
                sr = custom_types.SequenceRecordInformation(filename_list[0], filename_list[1], sequence, len(sequence), sequence.id, sequence.description)
                sequence_record_information.append(sr)
        return sequence_record_information


def create_edited_sequence_tupple(path, filename):
        filename_list=filename.split("_")
        segment_hemagglutinin = list(SeqIO.parse(path + filename, "fasta"))
        #For loop for turning the .fa files into a list of sequences that can be transformed  

        edited_sequence_record_information = []

        for sequence in segment_hemagglutinin: 
                segment_hemagglutinin_text = sequence.seq.upper()
                segment_hemagglutinin_sequence = Seq(segment_hemagglutinin_text)
                # print(len(segment_hemagglutinin_sequence))
                forward_sequence = segment_hemagglutinin_sequence[0:200]
                reverse_sequence = segment_hemagglutinin_sequence[-200:]
                esr = custom_types.EditedSequenceRecordInformation(filename_list[0], filename_list[1], forward_sequence, reverse_sequence, len(forward_sequence), len(reverse_sequence), sequence.id, sequence.description)
                edited_sequence_record_information.append(esr)
        return edited_sequence_record_information

def parse_primers(path, segment):
    segment_path = path + segment + "/primers/"
    segment_folder = os.scandir(segment_path)
    segments = [] 
    for entry in segment_folder:
        if entry.is_file():
            primer_tupple = create_primer_tupple(segment_path, entry.name)
            segments.append(primer_tupple)
    return segments

def parse_sequences(path, sequence):
    sequence_path = path + sequence + "/sequences/"
    sequence_folder = os.scandir(sequence_path)
    sequences = []
    for entry in sequence_folder:
        if entry.is_file():
            sequence_tupple = create_sequence_tupple(sequence_path, entry.name)
            sequences.append(sequence_tupple)
    return sequences

def parse_edited_sequences(path, edited_sequence):
    edited_sequence_path = path + edited_sequence + "/sequences/"
    edited_sequence_folder = os.scandir(edited_sequence_path)
    edited_sequenes = []
    for entry in edited_sequence_folder:
        if entry.is_file():
            edited_sequence_tupple = create_edited_sequence_tupple(edited_sequence_path, entry.name)
            edited_sequenes.append(edited_sequence_tupple)
    return edited_sequenes
