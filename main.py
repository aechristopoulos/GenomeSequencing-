import csv 
from Bio import SeqIO

file = open("sequences\A_Victoria_361_2011_H3N2_NP.fasta", "r")
# print(file.read())



with open("parsed_fasta_file.csv", "w") as csvfile:
    filewriter = csv.writer(csvfile, delimiter=',',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)



for seq_record in SeqIO.parse("sequences\A_Victoria_361_2011_H3N2_NP.fasta", "fasta"):
    print(seq_record.id)
    print(repr(seq_record.seq))
    print(len(seq_record))


