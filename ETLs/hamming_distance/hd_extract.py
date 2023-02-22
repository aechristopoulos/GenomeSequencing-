import hd_custom_types
import os 
from Bio import SeqIO


# Extract Function 
def extract(absolute_path):
    segment_information = {}
    path = absolute_path + "/db/"
    db = os.scandir(path)
    for entry in db: 
        if entry.is_dir():
            primer_info = parse_primers(path, entry.name)
            alignment_info = parse_alignments(path, entry.name)
            segment_information[entry.name] = hd_custom_types.DirectoryInformation(Primers=primer_info, Alignments=alignment_info)
    return segment_information

# create primer tupple function
def create_primer_tupple(path, filename): 
        primer_sequence = list(SeqIO.parse(path + filename, "fasta"))[0]
        filename_list = filename.split("_")
        primer_info = hd_custom_types.PrimerInformation(filename_list[0], filename_list[1], filename_list[2], filename_list[3] == "revcomp", primer_sequence.seq, primer_sequence.id, primer_sequence.description)
        return primer_info

# creates primer dictionary 
def parse_primers(path, segment):
    segment_path = path + segment + "/primers/"
    segment_folder = os.scandir(segment_path)
    segments = [] 
    for entry in segment_folder:
        if entry.is_file():
            primer_tupple = create_primer_tupple(segment_path, entry.name)
            segments.append(primer_tupple)
    return segments

#create aligment tupple function 
def create_alignment_tupple(path, filename):
     filename_list = filename.split("_")
     alignment_record = list(SeqIO.parse(path +filename, "fasta"))

     alignment_record_information = []

     for sequence in alignment_record: 
          ar = hd_custom_types.AlignmentInformation(filename_list[0], filename_list[1], sequence, sequence.id, sequence.description)
          alignment_record_information.append(ar)
     return alignment_record_information 

#create alignment dictionary function 
def parse_alignments(path, sequence): 
     alignment_path = path + sequence + "/alignments/"
     alignment_folder = os.scandir(alignment_path)
     alignments = []
     for entry in alignment_folder: 
          if entry.is_file():
               alignment_tupple = create_alignment_tupple(alignment_path, entry.name)
               alignments.append(alignment_tupple)
     return alignments