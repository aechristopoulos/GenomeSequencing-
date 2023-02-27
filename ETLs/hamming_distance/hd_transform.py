#imports 
from Bio import SeqIO
from scipy.spatial.distance import hamming
import re
import os


def transform(absolute_path, segment_information):
     path = absolute_path + "/db/"
     db = os.scandir(path)
     for entry in db: 
          if entry.is_dir():
               return do_transform(segment_information, entry.name)
    

def do_transform(segment_information, segment): 
     primer_info = segment_information[segment].Primers
     alignment_info = segment_information[segment].Alignments
     row_information = []
     for alignments in alignment_info:
          prime
     for primer in primer_info:
          for alignments in alignment_info:
               for sequence in alignments:
                   print(sequence.Description)
                   print(primer.Sequence.seq)
                   print(sequence.Sequence.seq)
                   print()
                   h_distance = indexing(primer.Sequence.seq, sequence.Sequence.seq)
                   row_information.append(results_row)
     return row_information

def find_primers(alignment_info):
     primers = []
     for alignments in alignment_info:
          for alignment in alignments:
               if "primer" in alignment.Description:
                    primers.append(alignment)
     return primers

def calc_hamming(primer, aligmments):
     hamming = []
     for alignment in aligmments: 
          h_distance = indexing(primer.Sequence.seq, alignment.Sequence.seq)
          results_row = {
                         "description": "", 
                         "strain_type": "",
                         "segment": "", 
                         "year": "",

                         "forward_sequence_subset": "", 
                         "reverse_sequence_subset": "",

                         "forward_primer": "",
                         "reverse_primer": "",

                         "forward_hamming_%":"",
                         "reverse_hamming_%":"",

                         "forward_hamming": h_distance,
                         "reverse_hamming": ""
                    }
          hamming.append(results_row)
     return hamming

def indexing(aligned_primer, aligned_sequence):
    primer_str = aligned_primer._data.decode("utf-8")
    sequence_str = aligned_sequence._data.decode("utf-8")
    first_index = re.search(r'[^-]', primer_str).start()
    second_index = re.search(r'[-]', primer_str[first_index:]).start()
    indexed_primer = primer_str[first_index:first_index + second_index]
    indexed_sequence = sequence_str[first_index:first_index + second_index]
    return hamming_distance(indexed_primer, indexed_sequence)

def convert(string):
    # Converts string to character separated list.
    # E.g., 'abcd' => ['a', 'b', 'c', 'd']
    list1=[]
    list1[:0]=string
    return list1 

def hamming_distance(indexed_primer, indexed_sequence):
    primer_array = convert(indexed_primer)
    sequence_array = convert(indexed_sequence)

    percent_hamming = hamming(primer_array, sequence_array)
    actual_hamming = percent_hamming *len(indexed_primer)
    return actual_hamming


#     for segment in segment_information:
#         pass

# def parse_row(primer_data, description, sequence, segment, is_forward=True):
#     row_distances = []

#     # Each primer to calculate hamming distance for
#     for i in range(0, len(primer_data), 2):
#         # Actual primer, and index to calculate hamming distance from.
#         # E.g., primer = 'ATGCATGCATGC', primer_idx = 174
#         primer, primer_idx = primer_data[i], int(primer_data[i + 1])
#         # 'ATGC' => ['A', 'T', 'G', 'C']
#         primer_list = convert(primer)

#         # Sequence subset to calculate hamming distance for.
#         # i.e., the part of the sequence we're checking the primer against
#         sequence_subset = sequence[primer_idx : primer_idx + len(primer_list)]
#         # 'ATGC' => ['A', 'T', 'G', 'C']
#         sequence_subset_list = convert(sequence_subset)

#         # Actual hamming distance given the sequnce_subset and the primer!
#         # Calculate as a percentage
#         hamming_distance = hamming(sequence_subset_list, primer_list)
#         # % of string * length of string is how many characters are different
#         primer_length = hamming_distance * len(primer_list)

#         # Description split into array by '/'
#         # e.g. AB/CD/EF/GH => ['AB', 'CD', 'EF', 'GH']
#         description_parts = description.split('/')
#         # Get last index in list.
#         # e.g. 'GH'
#         description_year_strain = description_parts[-1]
#         year = description_year_strain[0 : description_year_strain.index('(')]
#         strain_type = description_year_strain[description_year_strain.index('(') + 1 : description_year_strain.index(')')]

#         # Ternary expression in python
#         # https://www.geeksforgeeks.org/ternary-operator-in-python/
#         # Creates row for given primer against specific sequence
#         results_row = {
#             "description": description, 
#             "strain_type": strain_type,
#             "segment": segment, 
#             "year": year,

#             "forward_sequence_subset": sequence_subset if is_forward else "", 
#             "reverse_sequence_subset": sequence_subset if not is_forward else "",

#             "forward_primer": primer if is_forward else "",
#             "reverse_primer": primer if not is_forward else "",

#             "forward_hamming_%": hamming_distance if is_forward else "",
#             "reverse_hamming_%": hamming_distance if not is_forward else "",

#             "forward_hamming": primer_length if is_forward else "",
#             "reverse_hamming": primer_length if not is_forward else ""
#         }

#         row_distances.append(results_row)

#     return row_distances 