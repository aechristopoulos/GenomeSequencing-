import csv 
from Bio import SeqIO
import os

# Get the list of all files and directories
path = "./sequences"
dir_list = os.listdir(path)

if os.path.exists("parsed_file.csv"):
  os.remove("parsed_file.csv")
 

def my_function(filename):
    for seq_record in SeqIO.parse("sequences/" + filename, "fasta"):
        sequence_id = seq_record.id
        sequence = repr(seq_record.seq)
        sequence_length = len(seq_record)
    print(filename)
    write_to_csv(sequence_id, sequence, sequence_length)

def write_to_csv(sequence_id, sequence, sequence_length):
    with open("parsed_file.csv", "a") as csvfile:
        filewriter = csv.writer(csvfile, delimiter=',',
                             quotechar='|', quoting=csv.QUOTE_MINIMAL)
        filewriter.writerow(['sequence ID', sequence_id])
        filewriter.writerow(['sequence', sequence])
        filewriter.writerow(['sequence length', sequence_length])
    print(sequence_id)
    print(sequence)
    print(sequence_length)



for i in dir_list:
    my_function(i)

def main():
    return

if __name__ == "__main__":
    main()