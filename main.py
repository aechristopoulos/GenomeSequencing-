import csv 
from Bio import SeqIO
import os

# Get the list of all files and directories
path = ".\sequences"
dir_list = os.listdir(path)
 

def my_function(filename):
    for seq_record in SeqIO.parse("sequences\A_Victoria_361_2011_H3N2_NP.fasta", "fasta"):
        sequence_id = seq_record.id
        sequence = repr(seq_record.seq)
        sequence_length = len(seq_record)
    print(filename)
    print(sequence_id)
    print(sequence)
    print(sequence_length)

for i in dir_list:
    my_function(i)



# with open("parsed_fasta_file.csv", "w") as csvfile:
#     filewriter = csv.writer(csvfile, delimiter=',',
#                             quotechar='|', quoting=csv.QUOTE_MINIMAL)
#     filewriter.writerow(['sequence ID', sequence_id])
#     filewriter.writerow(['sequence', sequence])
#     filewriter.writerow(['sequence length', sequence_length])