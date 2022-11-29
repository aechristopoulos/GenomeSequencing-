import csv 
from Bio import SeqIO
import os


def main():
    # Get the list of all files and directories
    path = "./sequences"
    dir_list = os.listdir(path)

    data = []
    headers = ["Sequence ID", "Sequence", "Sequence Length"]

    if os.path.exists("parsed_file.csv"):
        os.remove("parsed_file.csv")
    
    for i in dir_list:
        my_function(i, data)

    write_to_csv(headers, data)

def my_function(filename,rows):
    for seq_record in SeqIO.parse("sequences/" + filename, "fasta"):
        sequence_id = seq_record.id
        sequence = repr(seq_record.seq)
        sequence_length = len(seq_record)
    rows.append([sequence_id, sequence, sequence_length])


def write_to_csv(header, data):
    with open("parsed_file.csv", "a") as csvfile:
        filewriter = csv.writer(csvfile, delimiter=',',
                             quotechar='|', quoting=csv.QUOTE_MINIMAL)
        filewriter.writerow(header)
        filewriter.writerows(data)
       
   


if __name__ == "__main__":
    main()