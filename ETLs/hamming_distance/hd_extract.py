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
            alignment_info = parse_alignments(path, entry.name)
            segment_information[entry.name] = hd_custom_types.DirectoryInformation(Alignments=alignment_info)
    return segment_information


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
