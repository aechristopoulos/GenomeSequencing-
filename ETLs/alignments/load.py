#imports 
from Bio.Align.Applications import ClustalOmegaCommandline
import subprocess
import os

# load function 
def load(absolute_path):
        path = absolute_path + "/db/"
        db = os.scandir(path)
        for entry in db: 
                if entry.is_dir():
                        #look at edited_sequences here
                        edited_sequences_path = path + entry.name + "/edited_sequences"
                        edited_sequences_folder = os.scandir(edited_sequences_path)
                        for sequences in edited_sequences_folder:
                                clustalomega_alignment(entry.name, sequences.name[:-6])

##ClustalOmega Alignment

def run_command(command):
        subprocess.run(["powershell", "-c"] + str(command).split())


def clustalomega_alignment(segment, filename): 
        in_file = "db/" + segment + "/edited_sequences/" + filename + ".fasta" 
        out_file = "db/" + segment + "/alignments/" + filename + "_alignment.fasta" 
        clustalomega_cline = ClustalOmegaCommandline(infile=in_file, outfile=out_file, verbose=True, auto=True)
        print(clustalomega_cline) 
        run_command(clustalomega_cline)