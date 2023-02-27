#imports 
from scipy.spatial.distance import hamming
import re

primer   = "AGCAAAAGCAGGGGATAATTCTATTAAC"
sequence = "AGCAAAAGCAGGGGAAAATAAAAGCAAC"

aligned_primer = "----------------------------------------------AGCAAAAGCAGGGGATAATTCTATTAAC---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------"
aligned_sequence = "----------------------------------------------AGCAAAAGCAGGGGAAAATAAAAGCAACCGAAATGAAGGCAAGACTATTAGTCTTGTTATGTGCATTTGCAGCTACAAA---------TGCAGACACACTATGTATAGGTTACCATGCAAATAACTCAACCGACACAGTTGACACAGTACTCGAGAAGAATGTAACCGTGACACACTCTGTTAACCTGCTTGAAGACAGCCACAACGGA--------------------------------" 

    
def indexing(aligned_primer, aligned_sequence):
    first_index = re.search(r'[^-]', aligned_primer).start()
    second_index = re.search(r'[-]', aligned_primer[first_index:]).start()
    indexed_primer = (aligned_primer[first_index:first_index + second_index])
    indexed_sequence = (aligned_sequence[first_index:first_index + second_index])
    return indexed_primer, indexed_sequence

print(indexing(aligned_primer, aligned_sequence))





def convert(string):
    # Converts string to character separated list.
    # E.g., 'abcd' => ['a', 'b', 'c', 'd']
    list1=[]
    list1[:0]=string
    return list1 

edited_primer = convert("AGCAAAAGCAGGGGATAATTCTATTAAC")
edited_sequence = convert("AGCAAAAGCAGGGGAAAATAAAAGCAAC")

percent_hamming = hamming(edited_primer, edited_sequence)
actual_hamming = percent_hamming * len(primer)
print(percent_hamming)
print(actual_hamming)

def hamming_distance(indexed_primer, indexed_sequence):
    primer_array = convert(indexed_primer)
    sequence_array = convert(indexed_sequence)

    percent_hamming = hamming(primer_array, sequence_array)
    actual_hamming = percent_hamming *len(indexed_primer)
    return actual_hamming

#  regular expressions: looking for the first occurance of not '-' in the string 

# x = re.search(r'[^-]', aligned_primer).start()
# y = re.search(r'[-]', aligned_primer[x:]).start()

# print(x)
# print(y)
# print(aligned_primer[x:x + y])
      