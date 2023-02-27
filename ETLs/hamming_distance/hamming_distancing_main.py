import csv
from hd_extract import extract
from hd_transform import transform
from hd_load import load_sequence_information

def hamming_distance_main(absolute_path):

    # E
    # Extract data from files, put it into a dictionary
    sequence_information = extract(absolute_path)
    hamming_distances = transform(absolute_path, sequence_information)
    load_sequence_information(absolute_path, hamming_distances)

    # # T
    # # Transform data within dictionary to what we'd like the rows to look like
    # hamming_distances = transform_sequence_information(sequence_information)

    # # L
    # # Save the rows to a file (.csv)
    # load_sequence_information(hamming_distances)