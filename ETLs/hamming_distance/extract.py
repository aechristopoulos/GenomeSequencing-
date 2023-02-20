import os

def extract_sequence_information():
    sequence_information = {}
    # For every folder (e.g. HA, NA, NP, PB1)
    for it in os.scandir():
        # We don't want to see hamming_distance.py
        if it.is_dir() and it.name != "__pycache__":
            # Folder name
            segment_name = it.name

            # Folder path
            gene_segment_folder = it.path

            # Each file within the folder
            for gene_segement in os.scandir(gene_segment_folder):
                filename = gene_segement.name

                # Path from current directory
                path = f"{gene_segment_folder}/{filename}"

                if gene_segement.name == "aligned_sequence":
                    with open(path, "r") as f:
                        aligned_sequence = f.read()

                if gene_segement.name == "forward_primer.txt":
                    with open(path, "r") as f:
                        forward_primer = f.read()

                if gene_segement.name == "reverse_primer.txt":
                    with open(path, "r") as f:
                        reverse_primer = f.read()

            # Dictionary value that contains information from each file
            files = (aligned_sequence, forward_primer.split("\n"), reverse_primer.split("\n"))

            sequence_information[segment_name] = files
            
    return sequence_information