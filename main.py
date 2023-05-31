import os
import sys

# Add path for local imports
absolute_path = os.getcwd()
sys.path.append(f"{absolute_path}/ETLs/alignments")
sys.path.append(f"{absolute_path}/ETLs/hamming_distance")
sys.path.append(f"{absolute_path}/ETLs/tree_alignments")

from ETLs.alignments.alignment_main import align
from ETLs.hamming_distance.hamming_distancing_main import hamming_distance_main
from ETLs.tree_alignments.tree_alignment_main import tree_alignment_main

def main():
    #align(absolute_path)
    hamming_distance_main(absolute_path)
    #tree_alignment_main(absolute_path)



if __name__ == "__main__":
    main()