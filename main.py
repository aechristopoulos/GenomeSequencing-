file = open("sequences\A_Victoria_361_2011_H3N2_NP.fasta", "r")
# print(file.read())

import csv 

with open("parsed_fasta_file.csv", "w") as csvfile:
    filewriter = csv.writer(csvfile, delimiter=',',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)

