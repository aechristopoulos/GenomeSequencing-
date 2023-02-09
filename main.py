import extract
import transform
import load

def main(): 
    segment_information = extract.extract()
    transform.transform(segment_information)



   
    

   


    






    

   


   
# def main():
# #     segments = ["PB2", "PB1", "PA", "HA", "NP", "NA", "MP", "NS"]
# #     for x in segments:
# #         primers = x.primer_fasta_files
# #         sequences = x.sequences
# #         do_etl(x, primers, sequences)
        

# def do_etl(segment_name, primers, sequences):
#     sequence_to_align_whatever_the_fuck = "HA_H5"

#     # Extract
#     HA_H5_alignment = alignment_functions.extract( sequence_to_align_whatever_the_fuck + "_sequences.fa") 
#     alignment_functions.print_sequence_record_info(HA_H5_alignment)

#     # Transform
#     for_seq_rec, rev_seq_rec = alignment_functions.sequence_record_objects(HA_H5_alignment)




#     alignment_functions.edited_sequences_fasta(for_seq_rec, "HA_H5_edited_forward.fasta")
#     alignment_functions.edited_sequences_fasta(rev_seq_rec, "HA_H5_edited_reverse.fasta")

#     # Load
#     for_alignment = alignment_functions.clustalw_alignment("HA_H5_edited_forward")
#     rev_alignment = alignment_functions.clustalw_alignment("HA_H5_edited_reverse")
    

if __name__ == "__main__":
    main()

# def main():
#     # Get the list of all files and directories
#     path = "./sequences"
#     dir_list = os.listdir(path)

#     data = []
#     headers = ["Sequence ID", "Sequence", "Sequence Length", "Sequence Name", "Sequence"]

#     if os.path.exists("parsed_file.csv"):
#         os.remove("parsed_file.csv")
    
#     for i in dir_list:
#         parse_fasta(i, data)

#     write_to_csv(headers, data)

# def parse_fasta(filename,rows):
#     record = list(SeqIO.parse("sequences/" + filename, "fasta"))

#     seq_record = record[0]

#     sequence_id = seq_record.id
#     sequence = repr(seq_record.seq)
#     sequence_length = len(seq_record)
#     sequence_name = seq_record.name
#     sequence_description = seq_record.description 


#     rows.append([sequence_id, sequence, sequence_length, sequence_name,sequence_description])


# def write_to_csv(header, data):
#     with open("parsed_file.csv", "a") as csvfile:
#         filewriter = csv.writer(csvfile, delimiter=',',
#                              quotechar='|', quoting=csv.QUOTE_MINIMAL)
#         filewriter.writerow(header)
#         filewriter.writerows(data)