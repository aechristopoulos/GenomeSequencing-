import csv
from hd_extract import extract
# from transform import transform_sequence_information
# from load import load_sequence_information

def hamming_distance_main(absolute_path):

    # E
    # Extract data from files, put it into a dictionary
    sequence_information = extract(absolute_path)

    # # T
    # # Transform data within dictionary to what we'd like the rows to look like
    # hamming_distances = transform_sequence_information(sequence_information)

    # # L
    # # Save the rows to a file (.csv)
    # load_sequence_information(hamming_distances)