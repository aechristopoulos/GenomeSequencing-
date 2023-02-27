import pandas as pd
from scipy.spatial.distance import hamming

def transform_sequence_information(sequence_information):
    rows = []

    # Each segment, e.g. MP, NA, NP, PB1, etc.
    for segment in sequence_information:
        # All sequences, along with their forward and reverse primers
        aligned_sequence, forward_primer_data, reverse_primer_data = sequence_information[segment]

        # Turn all sequences in xml format into Pandas Dataframes
        non_coding_region = pd.read_xml(aligned_sequence)
        #read .fasta files instead 
        # SeqIO.parse()
        

        # Each sequence
        for row in non_coding_region.iloc:
            description, _, sequence = row

            # Forward primer as transformed excel rows
            rows += parse_row(forward_primer_data, description, sequence, segment, is_forward=True)

            # Reverse primer as transformed excel rows
            rows += parse_row(reverse_primer_data, description, sequence, segment, is_forward=False)

    return rows

def parse_row(primer_data, description, sequence, segment, is_forward=True):
    row_distances = []

    # Each primer to calculate hamming distance for
    for i in range(0, len(primer_data), 2):
        # Actual primer, and index to calculate hamming distance from.
        # E.g., primer = 'ATGCATGCATGC', primer_idx = 174
        primer, primer_idx = primer_data[i], int(primer_data[i + 1])
        # 'ATGC' => ['A', 'T', 'G', 'C']
        primer_list = convert(primer)

        # Sequence subset to calculate hamming distance for.
        # i.e., the part of the sequence we're checking the primer against
        sequence_subset = sequence[primer_idx : primer_idx + len(primer_list)]
        # 'ATGC' => ['A', 'T', 'G', 'C']
        sequence_subset_list = convert(sequence_subset)

        # Actual hamming distance given the sequnce_subset and the primer!
        # Calculate as a percentage
        hamming_distance = hamming(sequence_subset_list, primer_list)
        # % of string * length of string is how many characters are different
        primer_length = hamming_distance * len(primer_list)

        # Description split into array by '/'
        # e.g. AB/CD/EF/GH => ['AB', 'CD', 'EF', 'GH']
        description_parts = description.split('/')
        # Get last index in list.
        # e.g. 'GH'
        description_year_strain = description_parts[-1]
        year = description_year_strain[0 : description_year_strain.index('(')]
        strain_type = description_year_strain[description_year_strain.index('(') + 1 : description_year_strain.index(')')]

        # Ternary expression in python
        # https://www.geeksforgeeks.org/ternary-operator-in-python/
        # Creates row for given primer against specific sequence
        results_row = {
            "description": description, 
            "strain_type": strain_type,
            "segment": segment, 
            "year": year,

            "forward_sequence_subset": sequence_subset if is_forward else "", 
            "reverse_sequence_subset": sequence_subset if not is_forward else "",

            "forward_primer": primer if is_forward else "",
            "reverse_primer": primer if not is_forward else "",

            "forward_hamming_%": hamming_distance if is_forward else "",
            "reverse_hamming_%": hamming_distance if not is_forward else "",

            "forward_hamming": primer_length if is_forward else "",
            "reverse_hamming": primer_length if not is_forward else ""
        }

        row_distances.append(results_row)

    return row_distances 

def convert(string):
    # Converts string to character separated list.
    # E.g., 'abcd' => ['a', 'b', 'c', 'd']
    list1=[]
    list1[:0]=string
    return list1
