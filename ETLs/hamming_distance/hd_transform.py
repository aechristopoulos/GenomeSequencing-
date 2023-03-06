#imports 
from Bio import SeqIO
from scipy.spatial.distance import hamming
import re
import os


def transform(absolute_path, segment_information):
     path = absolute_path + "/db/"
     db = os.scandir(path)
     rows = {}
     for entry in db: 
          if entry.is_dir():
               row_information = do_transform(segment_information, entry.name)
               rows[entry.name] = row_information
     return rows 
    

def do_transform(segment_information, segment): 
     alignment_info = segment_information[segment].Alignments
     row_information = {}
     for alignments in alignment_info:
          primers = find_primers(alignments)
          for primer in primers:
               h_distances = calc_hamming(primer, alignments)
               row_information[f"{alignments[0].Segment}_{alignments[0].Strain}_{primer.Id}"] = h_distances
     return row_information


def find_primers(alignment_info):
     primers = []
     for alignment in alignment_info:
          if "primer" in alignment.Description:
               primers.append(alignment)
     return primers


def calc_hamming(primer, aligmments):
     hamming = []
     for alignment in aligmments: 
          # print(primer.Description)
          # print(alignment.Description)
          # print()
          h_distance = indexing(primer.Sequence.seq, alignment.Sequence.seq)
          results_row = {
                         "description": alignment.Description, 
                         
                         "sequence": alignment.Sequence.seq,

                         "primer": primer.Sequence.seq,

                         "hamming_distance": h_distance
                    }
          hamming.append(results_row)
     return hamming

def indexing(aligned_primer, aligned_sequence):
    primer_str = aligned_primer._data.decode("utf-8")
    sequence_str = aligned_sequence._data.decode("utf-8")

    first_regex = re.search(r'[^-]', primer_str)
    first_index = first_regex.start()

    second_regex = re.search(r'[-]', primer_str[first_index:])
    second_index = len(primer_str[first_index:]) if second_regex is None else second_regex.start()

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


