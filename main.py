import os
import sys

# Add path for local imports
absolute_path = os.getcwd()
sys.path.append(f"{absolute_path}/ETLs/alignments")
sys.path.append(f"{absolute_path}/ETLs/hamming_distance")

from ETLs.alignments.alignment_main import align
from ETLs.hamming_distance.hamming_distancing_main import hamming_distance_main

def main():
    hamming_distance_main(absolute_path)

    # align(absolute_path)


if __name__ == "__main__":
    main()