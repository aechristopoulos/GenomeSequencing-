#imports 
from Bio.Seq import Seq
from Bio import SeqIO
from Bio import Align
from Bio.SeqRecord import SeqRecord
from Bio.Align.Applications import ClustalwCommandline
from Bio.Align.Applications import ClustalOmegaCommandline
from Bio import AlignIO
import subprocess
import os


# # Write forward primers
# def forward_primers(primer_sequence, id, description):
#   forward_primer = SeqRecord(Seq(primer_sequence), id = id, description = description)
#   forward_primer_record = SeqIO.write(forward_primer, "primer_fasta_files/" + id +"_primer.fasta", "fasta")
#   return forward_primer_record

# # Write reverse primers
# def reverse_primers(primer_sequence, id, description): 
#   reverse_primer = Seq(primer_sequence)
#   reverse_compliment = Seq(reverse_primer.reverse_compliment())
#   revcomp_primer = SeqRecord(Seq(reverse_compliment), id = id, description = description)
#   revcomp_primer_record = SeqIO.write(revcomp_primer, "primer_fasta_files/" + id +"primer.fasta", "fasta")
#   return revcomp_primer_record



###ClustalW alignment 
def clustalw_alignment(segment, filename):
        cline = ClustalwCommandline("clustalw2", infile= "db/" + segment + "/edited_sequences/" + filename + ".fasta")

        stdout, stderr = cline()

        align = AlignIO.read("/alignments/" + filename + ".aln", "clustal")
        return align


def load(command):
        path = "./db/"
        db = os.scandir(path)
        for entry in db: 
                if entry.is_dir():
                        run_command(command, entry.name)

##ClustalOmega Alignment

def run_command(command):
        subprocess.run(["powershell", "-c"] + str(command).split())


def clustalomega_alignment(segment, filename): 
        in_file = "db/" + segment + "/edited_sequences/" + filename + ".fasta" 
        out_file = "db/" + segment + "/alignments/" + filename + "_alignment.fasta" 
        clustalomega_cline = ClustalOmegaCommandline(infile=in_file, outfile=out_file, verbose=True, auto=True)
        print(clustalomega_cline) 
        run_command(clustalomega_cline)










