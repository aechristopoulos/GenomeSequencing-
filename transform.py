from Bio.Seq import Seq
from Bio import SeqIO
from Bio import Align
from Bio.SeqRecord import SeqRecord
from Bio.Align.Applications import ClustalwCommandline
from Bio import AlignIO
import custom_types



#Turning edited sequences into sequence record object to be used in alignments 
def sequence_record_objects(edited_sequence_record_information):
        forward_sequence_records = []
        reverse_sequence_records = []

        for record_information in edited_sequence_record_information: 
                forward_record = SeqRecord(record_information.ForwardSequence, id = record_information.Id, description = record_information.Description)
                reverse_record = SeqRecord(record_information.ReverseSequence, id = record_information.Id, description= record_information.Description)
                forward_sequence_records.append(forward_record)
                reverse_sequence_records.append(reverse_record)
        return forward_sequence_records, reverse_sequence_records


def primer_record_objects(primer_information):
        forward_primer_records = []
        reverse_primer_records = []

        for primer in primer_information:
                if primer.Direction == "Forward":
                        forward_primer = SeqRecord(primer.Sequence, id= primer.Id, description= primer.Description)
                        forward_primer_records.append(forward_primer)
                if primer.Direction == "Reverse": 
                        reverse_primer = SeqRecord(primer.Sequence, id = primer.Id, description= primer.Description)
                        reverse_primer_records.append(reverse_primer)
        return forward_primer_records, reverse_primer_records
        
# edited forward sequences to .fasta files 
def edited_forward_sequences_fasta(segment, filename, forward_sequence_records, forward_primers):
        edited_forward_record = forward_sequence_records + forward_primers
        SeqIO.write(edited_forward_record, "db/" + segment + "/edited_sequences/" + filename, "fasta")

#edited reverse sequences to .fasta files 
def edited_reverse_sequences_fasta(segment, filename, reverse_sequence_records, reverse_primers):
        edited_reverse_record = reverse_sequence_records + reverse_primers
        SeqIO.write(edited_reverse_record, "db/" + segment + "/edited_sequences/" + filename, "fasta")
